using System;
using System.Net.WebSockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Desktop.Network
{
    public class Connection
    {
        protected ClientWebSocket socket;
        protected CancellationToken cancellationToken;
        protected Uri uri;
        public Connection(Uri _uri)
        {
            uri = _uri;
            cancellationToken = new CancellationToken();
            socket = new ClientWebSocket();
            socket.ConnectAsync(uri, cancellationToken);
        }
        
        public async void SendMessage(string message)
        {
            socket = new ClientWebSocket();
            await socket.ConnectAsync(uri, cancellationToken);
            var bytes = Encoding.UTF8.GetBytes(message);
            var command = new ArraySegment<byte>(bytes);
            await socket.SendAsync(command, WebSocketMessageType.Text, true, new CancellationToken());
            socket.CloseAsync(WebSocketCloseStatus.NormalClosure, "", new CancellationToken());
        }
    }
}
