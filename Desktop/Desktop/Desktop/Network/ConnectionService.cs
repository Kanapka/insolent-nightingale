using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Net.WebSockets;

namespace Desktop.Network
{
    public class ConnectionService : IDisposable
    {
        protected Uri uri { get; }
        protected Queue<Message> OutgoingMessages { get; }
        protected CancellationToken Token { get; }
        protected CancellationTokenSource TokenSource { get; }
        public ConnectionService(Uri _uri, Queue<Message> _outgoingMessages)
        {
            uri = _uri;
            OutgoingMessages = _outgoingMessages;
            TokenSource = new CancellationTokenSource();
            Token = TokenSource.Token;
            Action RunWithToken = () => Run(Token);
            var task = Task.Run(RunWithToken);
        }
        public void AddMessage(Message message)
        {
            OutgoingMessages.Enqueue(message);
        }
        protected async void Run(CancellationToken cancellationToken)
        {
            var socket = new ClientWebSocket();
            socket = await Connection.OpenConnection(socket, "ws://localhost:443");
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
