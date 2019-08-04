using Desktop.Modules;
namespace Desktop.Commands
{
    public class LedCommand : ICommand
    {
        protected LedCommand(string _payload)
        {
            Payload = _payload;
        }

        public IModule Module => new LedModule();

        public static LedCommand On => new LedCommand("On");
        public static LedCommand Off => new LedCommand("Off");
        public static LedCommand Blink => new LedCommand("Blink");

        public string Payload { get; }

        public override string ToString()
        {
            return $"For module: {Module.Name}, command: {Payload}";
        }
    }
}
