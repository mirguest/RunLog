function handler() {
    if (this.readyState==4 && this.status==200) {
        document.getElementById("message").innerHTML=this.responseText;
    }
}

function newMsg() {
    var messagefrom = document.getElementById("messagefrom");
    var user = messagefrom.user.value;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange=handler;
    xmlhttp.open("POST", "/new", true);
    xmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
    xmlhttp.send("user="+user);

    var xmlhttp2 = new XMLHttpRequest();
    xmlhttp2.onreadystatechange=handler;
    xmlhttp2.open("POST", "/read", true);
    xmlhttp2.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
    xmlhttp2.send();

    return false;
}
