using Desktop.Messages;
using Desktop.Network;
using System;
using System.Collections.Generic;
using System.Windows;

namespace Desktop
{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application
    {
        protected ConnectionService connectionService;
        public App()
        {
        }
        protected override void OnStartup(StartupEventArgs e)
        {
            base.OnStartup(e);

            connectionService = new ConnectionService(
                new Uri("ws://localhost:443"),
                new Queue<IMessage>(),
                new System.Threading.CancellationTokenSource()
            );

            connectionService.Startup();
            var MainWindow = new MainWindow(connectionService);
            MainWindow.Show();
        }
    }
}
