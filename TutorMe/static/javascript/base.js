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
    FB.api(user, { locale: 'en_US', fields: 'first_name, last_name, email, picture.type(large)' }, function(api_response) {
            var postData = {fb: true};
            postData['email'] = api_response.email;
            postData['picture_url'] = api_response.picture.data.url;
            postData['first_name'] = api_response.first_name;
            postData['last_name'] = api_response.last_name;
            sendRequest(postData, postAddress);
    });
}

function sendRequest(postData, postAddress){
    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.post(postAddress, postData, function(data){
        console.log(data)
        var obj = JSON.parse(data);
        console.log(obj)
        if ("registered" in obj){
            if(!obj.registered){
                 
            }
        }
        if ("url" in obj) {
            window.location.href = obj.url;
        }
        return;
    })
}
