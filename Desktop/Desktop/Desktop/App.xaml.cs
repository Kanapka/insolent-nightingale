using Desktop.Commands;
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
        protected MessagingService connectionService;
        public App()
        {
        }
        protected override void OnStartup(StartupEventArgs e)
        {
            base.OnStartup(e);

            connectionService = new MessagingService(
                new Uri("ws://localhost:443"),
                new Queue<ICommand>(),
                new Queue<ICommand>(),
                new System.Threading.CancellationTokenSource()
            );

            var MainWindow = new MainWindow(connectionService);
            MainWindow.Show();
        }
    }
}
