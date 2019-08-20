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

        public static MobilityCommand Forward => new MobilityCommand("Forward");
        public static MobilityCommand Reverse => new MobilityCommand("Backward");
        public static MobilityCommand Left => new MobilityCommand("Left");
        public static MobilityCommand Right => new MobilityCommand("Right");
        public static MobilityCommand Stop => new MobilityCommand("Stop");
    }

}
