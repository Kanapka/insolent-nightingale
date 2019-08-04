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
        protected MessagingService ConnectionService { get; set; }
        public MainWindow(MessagingService _connectionService)
        {
            InitializeComponent();
            ConnectionService = _connectionService;
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
        protected override void OnClosing(CancelEventArgs e)
        {
            base.OnClosing(e);
            ConnectionService.Dispose();
        }
    }
}
