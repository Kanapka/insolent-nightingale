using System;
using System.Windows;
using Desktop.Network;
using Desktop.Commands;
using System.ComponentModel;

namespace Desktop
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private MessagingService ConnectionService { get; set; }
        public string ConnectionButtonText { get; set; }
        public MainWindow(MessagingService _connectionService)
        {
            InitializeComponent();
            ConnectionService = _connectionService;
            ConnectionButtonText = "Disconnected";
        }
        async void OnRequestTurnLedOn(object sender, EventArgs args)
        {
            ConnectionService.AddMessage(LedCommand.On);
        }
        async void OnRequestTurnLedOff(object sender, EventArgs args)
        {
            ConnectionService.AddMessage(LedCommand.Off);
        }
        async void OnRequestBlinkLed(object sender, EventArgs args)
        {
            ConnectionService.AddMessage(LedCommand.Blink);
        }
        async void OnConnectionClick(object sender, EventArgs args)
        {
            switch (ConnectionService.State)
            {
                case "Open":
                    ConnectionService.Disconnect();
                    ConnectionButtonText = "Disconnected";
                    break;
                case "Not connected":
                case "Closed":
                    ConnectionService.Startup();
                    ConnectionButtonText = "Connected";
                    break;
                case "Connecting":
                case "CloseReceived":
                case "CloseSent":
                default:
                    break;
            }
        }
        protected override void OnClosing(CancelEventArgs e)
        {
            base.OnClosing(e);
            ConnectionService.Dispose();
        }
    }
}
