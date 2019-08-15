using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Desktop.Commands
{
    public interface ICommand
    {
        string Type { get; }
        string Payload { get; }
    }
    public class CommandTypes
    {
        public static string Mobility => "MovementCommand";
        public static string RequestRange => "RangeCommand";
        public static string ReturnRange => "RangeResponse";
        public static string Led => "LedCommand";
    }
}
