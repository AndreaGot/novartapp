<!--
function SSstoCk(cdom,nm){var _st;if (cdom && cdom!="") {return 1;} if (window.opera) {return 1;}if (typeof(localStorage) == 'undefined' || typeof(sessionStorage) == 'undefined') {return 1;}else{if (!(_st = localStorage)) {return 1;}}return 0;}
function cCk(nm,vl,mn){var ex=cdm="";var okc=0;var _sscdom="";if (SSstoCk(_sscdom,nm)) {if (_sscdom && _sscdom!="") { cdm=" domain="+_sscdom; if (mn) {document.cookie=nm+"=; expires=Thu, 01-Jan-70 00:00:01 GMT; path=/;";}}if (mn) {var d=new Date();d.setTime(d.getTime()+(mn*6*1000)); ex="; expires="+d.toGMTString();} document.cookie=nm+"="+vl+ex+"; path=/;"+cdm+"";}else{if (mn) { _st = localStorage; }else{ _st = sessionStorage; }if (_st) { _st.setItem(nm,vl);}}}
function rCk(nm){ var fcoo=null;var nEQ=nm+"=";var ca=document.cookie.split(';'); var ses;if ((nm.indexOf("SV_")>-1)||(nm.indexOf("SSCDS_")>-1)){ses=1;}for(var i=0;i<ca.length;i++){var c=ca[i];while(c.charAt(0)==' ') c=c.substring(1,c.length); if(c.indexOf(nEQ) == 0){ fcoo=c.substring(nEQ.length,c.length);}}if (SSstoCk("",nm)) {return(fcoo);}else{ if (ses) { if (fcoo) {document.cookie=nm+"=; expires=Thu, 01-Jan-70 00:00:01 GMT; path=/;";return(fcoo);} _sstore = sessionStorage; }else{if (fcoo || fcoo=="") {document.cookie=nm+"=; expires=Thu, 01-Jan-70 00:00:01 GMT; path=/;";return(fcoo);} _sstore = localStorage;}return(_sstore.getItem(nm)); }}
function ud(){var u=""+o_.getTime();return(u);}
function udtb(){var u=""+otb_.getTime();return(u);}
function sswk_(tnow){var w = Math.floor( ( (tnow / 86400000 ) - 4) / 7);return w}
function stfCk(ck,v){var ca=_pt_=_iof_=can="";var _f_=uv_=uvw=1;var _tf_=ud();var _t_=_bu_=0;_ort=new Date();_ort.setTime(o_.getTime()+(1000*ssoffset_));if (!v) v=0;if (ck) {ca = ck.split('%G');_f_=parseInt(ca[2],10);_tf_=parseInt(ca[3],10);if (otb_.getTime()-parseInt(v,10)>st_){_ot=new Date();_ot.setTime(parseInt(_tf_,10)+(1000*ssoffset_)); if(_ort.getUTCMonth()==_ot.getUTCMonth()){_f_++;}else{_f_=1;_tf_=ud();}}_t_=ca[0];_pt_=ca[1];_bu_=ca[4];if (ca[5]) can=ca[5];} _ot=new Date();_ot.setTime(parseInt(_bu_,10)+(1000*ssoffset_));if ((_ort.getUTCDay()==_ot.getUTCDay())&&(_ort.getUTCMonth()==_ot.getUTCMonth())&&(_ort.getUTCFullYear()==_ot.getUTCFullYear())) uv_=0;if (sswk_(_ort) == sswk_(_ot)) uvw=0;_iof_=""+_t_+"%G"+_pt_+"%G"+_f_+"%G"+_tf_+"%G"+ud()+"%G";tf_="&FV="+_f_+"&UV="+uv_+"&US="+uvw;return(_iof_);}
function _ssuuid(len){var chars = '0123456789abcdef'.split('');var uuid = [], rnd = Math.random, r;uuid[8] = uuid[13] = uuid[18] = uuid[23] = '-';uuid[14] = '4';for (var i = 0; i < 36; i++){if (!uuid[i]){r = 0 | rnd()*16;uuid[i] = chars[(i == 19) ? (r & 0x3) | 0x8 : r & 0xf];}}return (len!==null) ? uuid.join('').replace(/-/g, '').split('',len).join('') : uuid.join('');}
function vscookie(){var cv="";var cs=au=rn="";if (us_.indexOf("vs-")>-1) {cv=rCk("SSKPI_"+us_);au=rCk("SSCDS_"+us_);rn=""+Math.round(Math.random()*2147483647); if (au) {if (au.indexOf(",")>-1) {var t=au.split(',');if (ud()-parseInt(t[1],10)<1800000) {cs=t[0];}}else cs=au;} if (cv) {if (!(cs)){cs=rn;}}else{cv=""+_ssuuid();cs=rn;}cCk("SSKPI_"+us_,cv,2592000); cCk("SSCDS_"+us_,cs+","+ud());var vsc="&SSKPI="+cv+"&SSCDS="+cs;return(vsc);}return("");}
function ssxl(xl_){var i_=new Image(1,1);i_.src="http://ssd3.paginegialle.it/cgi-bin/shinystat.cgi_pg?USER="+us_+"&"+xl_+vscookie()+"&RM="+Math.round(Math.random()*2147483647);i_.onload=function(){return;}; if (us_.indexOf("vs-")>-1){var ssinx_=new Image(1,1);ssinx_.src="http://nssd.paginegialle.it/cgi-bin/shinystat.cgi_pg?TLR=1&SSXL=1&USER="+us_+"&"+xl_+vscookie()+"&RM="+Math.round(Math.random()*2147483647);ssinx_.onload=function(){return;}}for(i=0;i<100000;i++);}
us_="vs-vetrerianovart";c_="";l_=""+screen.width;v_=navigator;d_=document.referrer;var o_=new Date();var otb_=new Date();vu_="&VUT=-1";n_="";tf_="";var st_=1800000;
o_.setTime(1000*1385759788); 
var ssoffset_=3600;
if (self != top){try {r_=""+escape(parent.document.referrer);}catch(e_r) {r_=""+escape(d_);}}
else {r_=""+escape(d_);}
k_="&CK="+(v_.cookieEnabled?"Y":"N");
j_="&JV="+(v_.javaEnabled()?"Y":"N");
hr_="&HR="+escape(window.location.href);
if(v_.appName!="Netscape"){c_=screen.colorDepth}
else{c_=screen.pixelDepth}
if (sv_ = rCk("SV_"+us_)){vu_="&VUT="+(otb_.getTime()-parseInt(sv_,10));}
cCk("SV_"+us_,udtb());
if (sn_=rCk("SN_"+us_)){ if (sn_=="ok") {sn_="";}cCk("SN_"+us_,stfCk(sn_,sv_,""),2592000);}else{n_="&NUT=y";cCk("SN_"+us_,stfCk("",sv_,""),2592000);}
var ssQs_="http://ssd3.paginegialle.it/cgi-bin/shinystat.cgi_pg?USER="+us_+"&REFER="+r_+"&COLOR="+c_+"&SIZE="+l_+k_+hr_+j_+vu_+n_+vscookie()+tf_+"&JS=Y&VJS=4005";
if (ssQs_.indexOf("RBOW=")>-1){var ssi_=new Image(1,1);ssi_.src=ssQs_+"&RM="+Math.round(Math.random()*2147483647);ssi_.onload=function(){return;}}
else{document.write("<img src=\""+ssQs_+"\" border=\"0\">");}
if (us_.indexOf("vs-")>-1){var ssin_=new Image(1,1);ssin_.src="http://nssd.paginegialle.it/cgi-bin/shinystat.cgi_pg?"+ssQs_.split("?")[1]+"&RM="+Math.round(Math.random()*2147483647);ssin_.onload=function(){return;}}
//-->

