using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Desktop.Network
{
    public class Message
    {
        protected string Content { get; set; }
        public Message(string _content)
        {
            Content = _content;
        }
        public override string ToString()
        {
            return Content;
        }
    }
}
