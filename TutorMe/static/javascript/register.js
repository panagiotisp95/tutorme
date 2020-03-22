/*
 * Function that assignes a listener to the checkboxes of the categories so that
 * when the user clicks on them the textarea in the form populated with the
 * selected categories
 */
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

/*
 * Function used to register the user using FB
 */
function register(){
    registerURL = $('#user_form').attr('action');
    attemptLogin(registerURL);
}

