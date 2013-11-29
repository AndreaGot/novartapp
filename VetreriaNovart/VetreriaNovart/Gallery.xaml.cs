using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Navigation;
using Microsoft.Phone.Controls;
using Microsoft.Phone.Shell;
using System.Windows.Controls;
using System.Collections.ObjectModel;
using System.Windows.Media.Imaging;
using System.Windows.Threading;

namespace VetreriaNovart
{
    public partial class Gallery : PhoneApplicationPage
    {

            private ObservableCollection _images;
            private int _currentIndex = 0;
            private DispatcherTimer timer = new DispatcherTimer();
            private const int INTERVAL = 3;
        public Gallery()
        {
            InitializeComponent();





InitializeImages();
AddEventHandlers();
InitializeTimer();
}

private void AddEventHandlers()
{
FadeOutAnimation.Completed += new EventHandler(FadeOutAnimation_Completed);
}

private void InitializeTimer()
{
timer.Interval = new TimeSpan(0, 0, 0, INTERVAL, 0);
timer.Tick += new EventHandler(timer_Tick);
timer.Start();
}

private void SetImageSource(string imageName)
{
string name = "Images/" + imageName;
BitmapImage bmi = new BitmapImage(new Uri(name, UriKind.Relative));
theImage.Source = bmi;
}

private void InitializeImages()
{
_images = new ObservableCollection() 
{ 
"Autumn Leaves.jpg",
"Creek.jpg",
"Desert Landscape.jpg",
"Dock.jpg",
"Forest Flowers.jpg",
"Forest.jpg"
}; 

SetImageSource(_images[_currentIndex]);
}

void FadeOutAnimation_Completed(object sender, EventArgs e)
{
SetImageSource(_images[_currentIndex]);
FadeInAnimation.Begin();
}

void timer_Tick(object sender, EventArgs e)
{
_currentIndex++;

if (_currentIndex == _images.Count)
{
_currentIndex = 0;
}

FadeOutAnimation.Begin();
}
        }
    }
