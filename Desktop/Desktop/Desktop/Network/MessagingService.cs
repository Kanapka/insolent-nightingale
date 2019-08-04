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
    public class MessagingService : IDisposable
    {
        protected Uri uri { get; }
        protected Queue<ICommand> OutgoingMessages { get; }
        protected Queue<ICommand> IncomingMessages { get; }
        protected CancellationToken Token { get; }
        protected CancellationTokenSource TokenSource { get; }
        protected int Sequence { get; set; }
        private readonly object queueLock = new object();

        public MessagingService(
            Uri _uri, 
            Queue<ICommand> _outgoingMessages,
            Queue<ICommand> _incomingMessages,
            CancellationTokenSource _tokenSource)
        {
            uri = _uri;
            OutgoingMessages = _outgoingMessages;
            IncomingMessages = _incomingMessages;
            TokenSource = _tokenSource;
            Token = TokenSource.Token;
            Sequence = 0;
        }
        public void Startup()
        {
            void RunWithToken() => Run(Token, uri);
            var task = Task.Run(RunWithToken);
        }
        public void AddMessage(ICommand message)
        {
            lock (queueLock)
            {
                OutgoingMessages.Enqueue(message);
            }
        }
        protected async void Run(CancellationToken cancellationToken, Uri uri)
        {
            var socket = new ClientWebSocket();
            socket = await Connection.OpenConnection(socket, uri);
            while (socket.State == WebSocketState.Open)
            {
                ICommand message = null;
                lock (queueLock)
                {
                    message = OutgoingMessages.Any() ? OutgoingMessages.Dequeue() : null;
                }
                if (message != null)
                {
                    await SendMessage(socket, message);
                }
                if (cancellationToken.IsCancellationRequested)
                {
                    await Cancel(socket);
                    cancellationToken.ThrowIfCancellationRequested();
                }
            }
            System.Diagnostics.Trace.WriteLine($"Connection closed. Reason: {socket.CloseStatus}, Details: {socket.CloseStatusDescription}");
        }

        protected async Task SendMessage(ClientWebSocket socket, ICommand message)
        {
            await Connection.SendMessage(socket, JsonConvert.SerializeObject(message));
            System.Diagnostics.Trace.WriteLine($"message {Sequence} sent");
            Sequence += 1;
        }

        protected async Task Cancel(ClientWebSocket socket)
        {
            await Connection.CloseConnection(socket);
            System.Diagnostics.Trace.WriteLine("Closing connection");
        }

        public void Dispose()
        {
            TokenSource.Cancel();
        }
    }
}
