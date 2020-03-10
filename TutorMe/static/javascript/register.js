$(document).ready(function () {
    $(".categories").change(function(){
        value = $('.categories').val();
        if ( value!="none" ) {
            var teacherCategories = $("#teacherCategories");
            var currentValue = teacherCategories.val();
            if (currentValue.includes(value) == false) {
                var text = currentValue + "," + value;
                if (currentValue == "") {
                    text = value;
                }
                teacherCategories.val(text);
            }
        }
    });
});
