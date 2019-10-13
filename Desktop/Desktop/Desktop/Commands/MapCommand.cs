using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Desktop.Commands
{
    class MapCommand : ICommand
    {
        public string Payload { get; }
        public string Type => CommandTypes.Map;
        private MapCommand() { }

        public static MapCommand New => new MapCommand();
    }
}
