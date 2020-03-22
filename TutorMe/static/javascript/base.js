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

function blink(selector) {
    $(selector).fadeOut(400, function() {
        $(selector).fadeIn(500);
    });

}

window.addEventListener( "pageshow", function ( event ) {
	var historyTraversal = event.persisted || ( typeof window.performance != "undefined" && window.performance.navigation.type === 2 );
	if ( historyTraversal ) {
		// Handle page restore.
		window.location.reload();
	}
});
