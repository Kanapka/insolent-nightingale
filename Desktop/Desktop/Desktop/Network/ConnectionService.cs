using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using System.Net.WebSockets;
using Desktop.Messages;

namespace Desktop.Network
{
    public class ConnectionService : IDisposable
    {
        protected Uri uri { get; }
        protected Queue<IMessage> OutgoingMessages { get; }
        protected CancellationToken Token { get; }
        protected CancellationTokenSource TokenSource { get; }
        public ConnectionService(
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
            OutgoingMessages.Enqueue(message);
        }
        protected async void Run(CancellationToken cancellationToken, Uri uri)
        {
            var socket = new ClientWebSocket();
            socket = await Connection.OpenConnection(socket, uri);
            int counter = 0;
            while (true)
            {
                if (OutgoingMessages.Any())
                {
                    var message = OutgoingMessages.Dequeue();
                    await Connection.SendMessage(socket, $"message no: {counter}, payload: {message}");
                    counter += 1;   
                }
                if (cancellationToken.IsCancellationRequested)
                {
                    await Connection.CloseConnection(socket);
                    Console.WriteLine("Closing connection");
                    cancellationToken.ThrowIfCancellationRequested();
                }
                Thread.Sleep(100);
            }
        }

        public void Dispose()
        {
            TokenSource.Cancel();
        }
    }
}
