using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using System.Net.WebSockets;
using Desktop.Network;

namespace Desktop.Messages
{
    public class MessagingService : IDisposable
    {
        protected Uri uri { get; }
        protected Queue<IMessage> OutgoingMessages { get; }
        protected CancellationToken Token { get; }
        protected CancellationTokenSource TokenSource { get; }
        private readonly object queueLock = new object();

        public MessagingService(
            Uri _uri, 
            Queue<IMessage> _outgoingMessages, 
            CancellationTokenSource _tokenSource)
        {
            uri = _uri;
            OutgoingMessages = _outgoingMessages;
            TokenSource = _tokenSource;
            Token = TokenSource.Token;

        }
        public void Startup()
        {
            Action RunWithToken = () => Run(Token, uri);
            var task = Task.Run(RunWithToken);
        }
        public void AddMessage(IMessage message)
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
            int counter = 0;
            while (socket.State == WebSocketState.Open)
            {
                IMessage message = null;
                lock (queueLock)
                {
                    message = OutgoingMessages.Any() ? OutgoingMessages.Dequeue() : null;
                }
                if (message != null)
                {
                    await Connection.SendMessage(socket, $"message no: {counter}, payload: {message}");
                    System.Diagnostics.Trace.WriteLine($"message {counter} sent");
                    counter += 1;   
                }
                if (cancellationToken.IsCancellationRequested)
                {
                    await Connection.CloseConnection(socket);
                    System.Diagnostics.Trace.WriteLine("Closing connection");
                    cancellationToken.ThrowIfCancellationRequested();
                }
            }
            System.Diagnostics.Trace.WriteLine($"Connection closed. Reason: {socket.CloseStatus}, Details: {socket.CloseStatusDescription}");
        }

        public void Dispose()
        {
            TokenSource.Cancel();
        }
    }
}
