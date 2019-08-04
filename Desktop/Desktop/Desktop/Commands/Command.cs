using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Desktop.Modules;

namespace Desktop.Commands
{
    public interface ICommand
    {
        IModule Module { get; }
        string Payload { get; }
    }
}
