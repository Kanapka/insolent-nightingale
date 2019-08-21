using System;
using System.Windows;
using Desktop.Network;
using Desktop.Commands;
using System.ComponentModel;
using Desktop.Movement;
using System.Threading;
using System.Windows.Input;
using System.Runtime.CompilerServices;

namespace Desktop
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window, INotifyPropertyChanged
    {
        private string _connectionButtonText;

        public event PropertyChangedEventHandler PropertyChanged;

        private IMessagingService ConnectionService { get; set; }
        public string ConnectionButtonText
        {
            get => _connectionButtonText ?? "-";
            set
            {
                _connectionButtonText = value;
                NotifyPropertyChanged();
            }
        }
        public MainWindow(MessagingService _connectionService) 
        {
            InitializeComponent();
            ConnectionService = _connectionService;
            ConnectionService.OnConnecting = OnConnecting;
            ConnectionService.OnConnected = OnConnect;
            ConnectionService.OnDisconnect = OnDisconnect;
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
        void OnConnect()
        {
            ConnectionButtonText = "Connected";
        }
        void OnConnecting()
        {
            ConnectionButtonText = "Connecting";
        }
        void OnDisconnect()
        {
            ConnectionButtonText = "Disconnected";
        }
        async void OnConnectionClick(object sender, EventArgs args)
        {
            switch (ConnectionService.State)
            {
                case "Open":
                    ConnectionService.Disconnect();
                    break;
                case "Not connected":
                case "Closed":
                    ConnectionService.Startup();
                    break;
                case "Connecting":
                case "CloseReceived":
                case "CloseSent":
                default:
                    break;
            }
        }
        async void OnKeyDown(object sender, EventArgs args)
        {
            var controller = new MovementController(this.ConnectionService);
            var key = (args as KeyEventArgs)?.Key;
            switch (key)
            {
                case Key.W:
                    controller.Forward();
                    break;
                case Key.A:
                    controller.TurnLeft();
                    break;
                case Key.S:
                    controller.Backward();
                    break;
                case Key.D:
                    controller.TurnRight();
                    break;
            }
        }
        async void OnKeyUp(object sender, EventArgs args)
        {
            var controller = new MovementController(this.ConnectionService);
            controller.Stop();
        }
        private void NotifyPropertyChanged([CallerMemberName] String propertyName = "")
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }

        private void Main_Closing(object sender, CancelEventArgs e)
        {
            ConnectionService.Disconnect();
        }
    }
}
