function Req(url,callback){
    var Xhr;
    if (window.XMLHttpRequest)
    {// code for IE7+, Firefox, Chrome, Opera, Safari
        Xhr=new XMLHttpRequest();
    }
    else
    {// code for IE6, IE5
        Xhr=new ActiveXObject("Microsoft.XMLHTTP");
    }
    Xhr.onreadystatechange = function(){
        if(Xhr.readyState==4&&Xhr.status==200){
            callback(Xhr.responseText);
        }
    }
    Xhr.open("GET",url,true);
    Xhr.send();
    
}


