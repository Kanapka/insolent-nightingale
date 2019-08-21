using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using System.Net.WebSockets;
using Desktop.Commands;
using Newtonsoft.Json;


namespace Desktop.Network
{
    public class MessagingService : IMessagingService
    {
        public string State => WebSocket?.State.ToString() ?? "Not connected";
        private ClientWebSocket WebSocket { get; set; }
        private Uri Uri { get; }
        private Queue<ICommand> OutgoingMessages { get; }
        private Queue<ICommand> IncomingMessages { get; }
        private CancellationToken Token { get; set; }
        private CancellationTokenSource TokenSource { get; set; }
        private readonly object queueLock = new object();

        public Action OnConnecting { get; set; }
        public Action OnConnected { get; set; }
        public Action OnDisconnect { get; set; }

        public MessagingService(
            Uri _uri, 
            Queue<ICommand> _outgoingMessages,
            Queue<ICommand> _incomingMessages)
        {
            Uri = _uri;
            OutgoingMessages = _outgoingMessages;
            IncomingMessages = _incomingMessages;;
        }
        public void Startup()
        {
            TokenSource = new CancellationTokenSource();
            Token = TokenSource.Token;
            void RunWithToken() => Run(Token, Uri);
            var task = Task.Run(RunWithToken);
        }
        public void AddMessage(ICommand message)
        {
            lock (queueLock)
            {
                OutgoingMessages.Enqueue(message);
            }
        }
        public async void Disconnect()
        {
            TokenSource.Cancel();
        }
        protected async void Run(CancellationToken cancellationToken, Uri uri)
        {
            WebSocket = new ClientWebSocket();
            OnConnecting();
            WebSocket = await Connection.OpenConnection(WebSocket, uri);
            if(WebSocket.State == WebSocketState.Open)
            {
                OnConnected();
            }
            while (WebSocket.State == WebSocketState.Open)
            {
                if (cancellationToken.IsCancellationRequested)
                {
                    await Cancel(WebSocket);
                    break;
                }
                ICommand message = null;
                lock (queueLock)
                {
                    message = OutgoingMessages.Any() ? OutgoingMessages.Dequeue() : null;
                }
                if (message != null)
                {
                    await SendMessage(WebSocket, message);
                }
            }
            System.Diagnostics.Trace.WriteLine($"Connection closed. Reason: {WebSocket.CloseStatus}, Details: {WebSocket.CloseStatusDescription}");
            OnDisconnect();
        }

        protected async Task SendMessage(ClientWebSocket socket, ICommand message)
        {
            await Connection.SendMessage(socket, JsonConvert.SerializeObject(message));
        }

        protected async Task Cancel(ClientWebSocket socket)
        {
            await Connection.CloseConnection(socket);
            System.Diagnostics.Trace.WriteLine("Closing connection");
            OnDisconnect();
        }

        public void Dispose()
        {
            Disconnect();
        }
    }
}
