using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Desktop.Messages
{
    public interface IMessage { }
    public class Message : IMessage
    {
        protected string Content { get; set; }

        public static IMessage ForwardOrder => new Message("Forward!");
        public static IMessage ReverseOrder => new Message("Backward!");

        protected Message(string _content)
        {
            Content = _content;
        }
        public override string ToString()
        {
            return Content;
        }
    }
}
