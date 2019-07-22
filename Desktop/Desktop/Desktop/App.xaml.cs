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
        protected Func<Connection> CreateConnection;
        protected Func<Uri> CreateUri;
        protected Func<MainWindow> CreateMainWindow;
        public App()
        {
            Bootstrap();
        }
        protected override void OnStartup(StartupEventArgs e)
        {
            base.OnStartup(e);
            this.MainWindow = CreateMainWindow();
            this.MainWindow.Show();
        }
        public void Bootstrap()
        {
            CreateUri = () => new Uri("ws://localhost:443");
            CreateConnection = () => new Connection(CreateUri());
            CreateMainWindow = () => new MainWindow(CreateConnection());
        }
    }
}
