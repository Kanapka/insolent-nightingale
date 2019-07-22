using System;
using System.Windows;
using Desktop.Network;
using Desktop.Messages;
using System.ComponentModel;

namespace Desktop
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        protected MessagingService ConnectionService { get; set; }
        public MainWindow(MessagingService _connectionService)
        {
            InitializeComponent();
            ConnectionService = _connectionService;
        }
        async void OnSendMessage(object sender, EventArgs args)
        {
            ConnectionService.AddMessage(Message.ForwardOrder);
        }
        protected override void OnClosing(CancelEventArgs e)
        {
            base.OnClosing(e);
            ConnectionService.Dispose();
        }
    }
}
