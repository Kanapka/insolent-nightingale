using Desktop.Commands;
using System;

namespace Desktop.Network
{
    public interface IMessagingService : IDisposable

    {
        string State { get; }
        Action OnConnecting { get; set; }
        Action OnConnected { get; set; }
        Action OnDisconnect { get; set; }

        void Startup();
        void AddMessage(ICommand message);
        void Disconnect();
    }
}
