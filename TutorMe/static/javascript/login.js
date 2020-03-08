$(document).ready(function () {
    $(".animated-text").typed({
        strings: [
            "Are you a teacher?",
            "Are you a student?",
            "You are at the right place!"
        ],
        smartBackspace: true,
        typeSpeed: 50,
        loop: true,
        backSpeed: 50,
        backDelay: 50,
    });
});

function attemptLogin(){
    koko = null;
    FB.getLoginStatus(function(response) {
        if(response){
            if(response.status == "unknown"){
                console.log(response);
                koko = "lo";
            }else{
                sendRequest(response);
            }
        }else{
            console.log("not able to get response");
        }
    }, true);

    if(koko == "lo"){
    console.log("sss");
    }
}

function login(){
    FB.login(function(response) {
        console.log(response);
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function sendRequest(data){
    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.post('/tutorme/login/',{koko :'lolo'},function(data){
        console.log(data);
    })
}
