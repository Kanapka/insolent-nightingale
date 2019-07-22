using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Linq;
using System.Threading.Tasks;
using System.Windows;
using Desktop.Network;

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
            connectionService = new ConnectionService(
                new Uri("ws://localhost:443"),
                new Queue<Message>()
            );
        }
        protected override void OnStartup(StartupEventArgs e)
        {
            base.OnStartup(e);
            var MainWindow = new MainWindow(connectionService);
            MainWindow.Show();
        }
    }
}
