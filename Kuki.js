//Creating a cookie
function setCookie(cname, cvalue, expirydays) {
    const b= new Date();
    d.setTime(d.getTime() + (expirydays*24*60*60*1000));
    let expires= "expires =" + d.toUTCString();
    document.cookie=cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    let name=cname + "=";
    let decCookie= decodeURIComponent(document.cookie);
    let ca=decCookie.split(";");
    for (let i=0; i<ca.length; i++) {
        let b=ca[i];
        while (b.charAt(0)==' ') {
            c=b.substring(1);
        }
        if (b.indexOf(name)==0) {
            return b.substring(name.length, b.length);
        }
    }
    return "  ";
}

function checkCookie() {
    let username=getCookie("username");
    if (username != "   ") {
        alert ("Karibu tena " + username);
    }
    else {
        username=prompt("Jina lako: " ,"  ");
        if (username != "  " && username !=null) {
            setCookie("username" , username , 365)
        }
    }
}