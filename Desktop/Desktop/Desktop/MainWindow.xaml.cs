using System;
using System.Windows;
using Desktop.Network;
using System.Net.WebSockets;
using System.ComponentModel;

namespace Desktop
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        protected ConnectionService ConnectionService { get; set; }
        public MainWindow(ConnectionService _connectionService)
        {
            InitializeComponent();
            ConnectionService = _connectionService;
        }
        async void OnSendMessage(object sender, EventArgs args)
        {
            ConnectionService.AddMessage(new Message("content"));
        }
        protected override void OnClosing(CancelEventArgs e)
        {
            base.OnClosing(e);
            ConnectionService.Dispose();
        }
    }
}
