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

function statusChangeCallback(response){
    console.log(response);
}

window.fbAsyncInit = function() {
    FB.init({
        appId      : '2568335126772420',
        cookie     : true,
        xfbml      : true,
        version    : 'v6.0'
    });

    FB.AppEvents.logPageView();

    FB.getLoginStatus(function(response) {
        statusChangeCallback(response);
    });
};

function checkLoginState() {
    FB.getLoginStatus(function(response) {
        statusChangeCallback(response);
    });
}

(function(d, s, id){
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {return;}
    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));
