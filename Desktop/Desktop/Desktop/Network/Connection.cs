using System;
using System.Net.WebSockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Desktop.Network
{
    public class Connection
    {
        public static async Task<ClientWebSocket> OpenConnection(ClientWebSocket socket, Uri _uri)
        {
            try
            {
                await socket.ConnectAsync(_uri, new CancellationToken());
            }
            catch (Exception ex)
            {
                ;
            }
            return socket;
        }
        public static async Task<ClientWebSocket> CloseConnection(ClientWebSocket socket)
        {
            await socket.CloseAsync(
                WebSocketCloseStatus.NormalClosure, 
                "", 
                new CancellationToken());
            return socket;
        }
        public static async Task SendMessage(ClientWebSocket socket, string message)
        {
            var bytes = Encoding.UTF8.GetBytes(message);
            var command = new ArraySegment<byte>(bytes);
            await socket.SendAsync(command, WebSocketMessageType.Text, true, new CancellationToken());
        }
    }
}
