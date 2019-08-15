namespace Desktop.Commands
{
    class MobilityCommand : ICommand
    {
        public string Payload { get; }
        public string Type => CommandTypes.Mobility;
        private MobilityCommand(string _payload)
        {
            Payload = _payload;
        }

        public MobilityCommand Forward => new MobilityCommand("Forward");
        public MobilityCommand Reverse => new MobilityCommand("Backward");
        public MobilityCommand Left => new MobilityCommand("Left");
        public MobilityCommand Right => new MobilityCommand("Right");
        public MobilityCommand Stop => new MobilityCommand("Stop");
    }

}
