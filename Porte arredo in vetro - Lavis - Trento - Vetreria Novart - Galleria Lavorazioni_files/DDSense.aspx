function DD()
{
var n = new Date();
var sTimezone = n.getTimezoneOffset();
var sWidth=screen.width;
var sHeight=screen.height;
var sApp=navigator.appName;
var sReferrer=""+escape(document.referrer);
var sLocation=""+escape(document.URL);
var sColor=0;
if (sApp!="Netscape") sColor=screen.colorDepth;
else sColor=screen.pixelDepth;
document.write(
	"<div id=\"Layer2\" style=\"position:absolute;\"><img src=\"http://visual-lead.seat.it/Sensor/DDWebSensor.aspx?id=seat_vl_0013342_2731268&keywords="+
	"&rnd="+Math.random()+
	"&location="+sLocation+
	"&referrer="+sReferrer+
	"&color="+sColor+
	"&width="+sWidth+
	"&height="+sHeight+
	"&timezone="+sTimezone+
	"\" width=\"1\" height=\"1\" ></div>"); 
}

function DD2()
{
var n = new Date();
var sTimezone = n.getTimezoneOffset();
var sWidth=screen.width;
var sHeight=screen.height;
var sApp=navigator.appName;
var sReferrer=""+escape(document.referrer);
var sLocation=""+escape(document.URL);
var sColor=0;
if (sApp!="Netscape") sColor=screen.colorDepth;
else sColor=screen.pixelDepth;
document.write(
	"<div id=\"Layer2\" style=\"position:absolute;\"><img src=\"http://visual-lead.seat.it/Sensor/DDWebSensor.aspx?id=seat_vl_0013342_2731268&keywords="+
	"&rnd="+Math.random()+
	"&location="+sLocation+
	"&referrer="+sReferrer+
	"&color="+sColor+
	"&width="+sWidth+
	"&height="+sHeight+
	"&timezone="+sTimezone+
	"\" width=\"1\" height=\"1\" ></div>"); 
}

//DD();
DD2();