$(document).ready(function () {
    $( "li" ).find("input").change(function(){
        var selected_categories = $("#selected_categories");
        var currentValue = selected_categories.val();
        label = "label[for='"+this.id+"']";
        value = $(label).text().replace(/[^0-9a-z]/gi, '');

        if($(this).is(":checked")){
            if (currentValue.includes(value) == false) {
                var text = currentValue + "," + value;
                if (currentValue.charAt(text.length-1) == ","){
                    text = currentValue + value;
                }
                if (currentValue == "") {
                    text = value;
                }
            }
        }else{
            if (currentValue.includes(value)) {
                var text = currentValue.replace(value+",",'');
                if (text == currentValue){
                    text = currentValue.replace(","+value,'');
                    if (text == currentValue){
                        text = currentValue.replace(value,'');
                    }
                }
            }
        }
        selected_categories.val(text);
    });
});

function register(){
    registerURL = $('#user_form').attr('action');
    attemptLogin(registerURL);
}

