using System;
using System.Collections.Generic;
using Desktop.Network;
using Desktop.Commands;

namespace Desktop.Movement
{
    public class MovementController
    {
        private IMessagingService MessagingService { get; set; }
        public MovementController(IMessagingService messagingService)
        {
            this.MessagingService = messagingService;
        }
        public void Stop()
        {
            MessagingService.AddMessage(MobilityCommand.Stop);
        }
        public void Forward()
        {
            MessagingService.AddMessage(MobilityCommand.Forward);
        }
        public void Backward()
        {
            MessagingService.AddMessage(MobilityCommand.Reverse);
        }
        public void TurnRight()
        {
            MessagingService.AddMessage(MobilityCommand.Right);
        }
        public void TurnLeft()
        {
            MessagingService.AddMessage(MobilityCommand.Left);
        }
    }
}
