using System;
using System.Windows;
using Desktop.Network;

namespace Desktop
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        protected Connection Connection { get; set; }
        public MainWindow(Connection _connection)
        {
            InitializeComponent();
            Connection = _connection;
        }
        void OnSendMessage(object sender, EventArgs args)
        {
            Connection.SendMessage("message");
        }
    }
}
