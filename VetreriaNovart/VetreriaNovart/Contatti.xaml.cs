using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Navigation;
using Microsoft.Phone.Controls;
using Microsoft.Phone.Shell;
using Microsoft.Phone.Tasks; 

namespace VetreriaNovart
{
    public partial class Contatti : PhoneApplicationPage
    {
        public Contatti()
        {
            InitializeComponent();
        }

        private void btnInvia_Click(object sender, RoutedEventArgs e)
        {

            String body = txtNome.Text + " ha inviato questa richiesta: " + txtRichiesta.Text;

            var emailcomposer = new EmailComposeTask
            {
                To = "mailto:vetrerianovart@alice.it",
                Subject = "Richiesta Informazioni - WP",

                Body = body,
                
            };

            emailcomposer.Show();
        }







    }
}