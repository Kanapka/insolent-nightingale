using Desktop.Commands;
using System;

namespace Desktop.Network
{
    interface IMessagingService : IDisposable

    {
        string State { get; }
        void Startup();
        void AddMessage(ICommand message);
        void Disconnect();
    }
}
