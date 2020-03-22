/*
 * Function used to get a value from cookie given a name
 */
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

/*
 * Function used to check if the HTTP methods do not require CSRF protection
 */
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/*
 * Function used to login using facebook
 */
function attemptLogin(postAddress){
    FB.login(function(login_response) {
        if(login_response){
            if (login_response.authResponse) {
                getUserDetails(login_response);
            }else{
                console.log(login_response, postAddress);
            }
        }else{
            console.log("not able to get response");
        }
    }, {scope: 'email'});
}

/*
 * Function used by the login above to fetch the user details,
 * Also it sends a request to the backend to attempt to login the user
 */
function getUserDetails(login_response, postAddress){
    var id = login_response.authResponse.userID;
    var user = '/'+id+'/';
    FB.api(user, { locale: 'en_US', fields: 'first_name, last_name, email' }, function(api_response) {
            var postData = {fb: true};
            postData['email'] = api_response.email;
            postData['first_name'] = api_response.first_name;
            postData['last_name'] = api_response.last_name;
            sendRequest(postData, postAddress);
    });
}

/*
 * Function used to setup ajax so that has the csrftoken in the request
 */
function ajaxSetup(){
    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
}

/*
 * Function used to send the post request to the backend and checks if the
 * user is successfully registered and redirects to the homepage or prints
 * a message to register first and then login
 */
function sendRequest(postData, postAddress){
    ajaxSetup();

    $.post(postAddress, postData, function(data){
        console.log(data)
        var obj = JSON.parse(data);
        console.log(obj)
        if ("registered" in obj){
            if(!obj.registered){
                let timerId = setInterval(blink, 1200, "#registerStudent");
                let timerId1 = setInterval(blink, 1200, "#registerTeacher");
                $("#errorMessage").append("<p>Currently you are not a user please use the buttons on the left to Register!</p>");
            }
        }
        if ("url" in obj) {
            window.location.href = obj.url;
        }
        return;
    });
}

/*
 * Function used to blink the register buttons to highlight to the user
 * where to click in order to register
 */
function blink(selector) {
    $(selector).fadeOut(400, function() {
        $(selector).fadeIn(500);
    });

}

/*
 * refresh the page when a user uses the back arrow of the browser
 */
window.addEventListener( "pageshow", function ( event ) {
	var historyTraversal = event.persisted || ( typeof window.performance != "undefined" && window.performance.navigation.type === 2 );
	if ( historyTraversal ) {
		// Handle page restore.
		window.location.reload();
	}
});
