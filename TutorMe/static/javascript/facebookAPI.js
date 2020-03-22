/*
 * Function to get fb callback
 */
function statusChangeCallback(response){
    console.log(response);
}

/*
 * Function provided by fb developers site to initialise FB API variable
 */
window.fbAsyncInit = function() {
    FB.init({
        appId      : '2568335126772420',
        cookie     : true,
        xfbml      : true,
        version    : 'v6.0'
    });

    FB.AppEvents.logPageView();
};

/*
 * Function to get login status
 */
function checkLoginState() {
    FB.getLoginStatus(function(response) {
    }, true);
}

/*
 * Function needed for facebook API
 */
(function(d, s, id){
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {return;}
    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));
