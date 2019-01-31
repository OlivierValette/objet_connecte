function lighter(cible, onoff) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET","http://192.168.2.14:5000/" + onoff + (cible == '' ? '' : '/') + cible, false);
    xmlHttp.send(null);
    console.log("http://192.168.2.14:5000/" + onoff + (cible == '' ? '' : '/') + cible);
    return xmlHttp.responseText;
}
