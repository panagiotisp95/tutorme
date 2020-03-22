$(document).ready(function() {
    /*
     * Visualizing things on Hover over the stars so the user knows
     */
    $('.stars li').on('mouseover', function(){

        var onStar = parseInt($(this).data('value'), 10); // The star currently mouse on

        // Now highlight all the stars that's not after the current hovered star
        $(this).parent().children('li.star').each(function(e){
            if (e < onStar) {
                $(this).addClass('hover');
            }else{
                $(this).removeClass('hover');
            }
        });
    }).on('mouseout', function(){
        $(this).parent().children('li.star').each(function(e){
            $(this).removeClass('hover');
        });
    });

    /*
     * Action to perform on click of the stars
     */
    $('.stars li').on('click', function(){
        var onStar = parseInt($(this).data('value'), 10); // The star currently selected
        var stars = $(this).parent().children('li.star');

        for (i = 0; i < stars.length; i++) {
            $(stars[i]).removeClass('selected');
        }

        for (i = 0; i < onStar; i++) {
            $(stars[i]).addClass('selected');
        }

        // JUST RESPONSE (Not needed)
        var ratingValue = parseInt($('.stars li.selected').last().data('value'), 10);
        var name = $(".stars").parent().parent().attr('class');
        var str = $(".stars").parent().parent().attr('about');
        var res = str.split(" ");

        console.log(name);
        console.log(ratingValue);
        $('body').append('<div id="yesno_dialog" title="Yes Or No"><p>Submit review?</p></div>');
        $("#yesno_dialog").dialog({
            title: "Yes or No",
            resizable: false,
            modal: true,
            buttons: {
                "Yes" : function () {
                    rate(res[0], res[1], res[2], name, ratingValue)

                    $(this).dialog("close");
                    $(this).remove();
                },
                "No" : function (){
                    $(this).dialog("close");
                    $(this).remove();
                }

            }
        });
    });


});

/*
 * Function used to make a post request in order to rate the teacher that the student
 * clicked
 */
function rate(teacher_email, student_email, url, teacher_name, ratingValue){
    var postData = {"teacher_email": teacher_email, "student_email": student_email, "rating": ratingValue};

    ajaxSetup();
    $.post(url, postData, function(data){
        if(data == "ok"){
            var koko = "#"+teacher_name;
            $(koko).remove();
            $("#stars_rating_for_user_"+teacher_name).append('<div class="Stars" style="--rating: '+ ratingValue +';"></div>');
        }
        return;
    })
}
