/*
 * Sets the autocomplete options and add the categories initialised
 * in the html as data
 */
var options = {
    data : categories,

    list: {
        maxNumberOfElements: 8,
        match: {
            enabled: true
        },
        sort: {
            enabled: true
        }
    },
};

/*
 * Adds the autocomplete to the chosen text input
 */
$("#search_box").easyAutocomplete(options);

/*
 * Function executes when a user presses the accept button on a teacher card
 * and sends a post request so that they are linked and could see each other
 * in their dashboards
 */
function accept(teacher_email, teacher_name, url, student){
    var postData = {"teacher_email": teacher_email, "student_email": student};

    ajaxSetup();
    $.post(url, postData, function(data){
        if(data == "ok"){
            var name = "#accepted_"+teacher_name+" p"
            $(name ).text( "Accepted" );
        }else if(data="Already"){
            var name = "#accepted_"+teacher_name+" p"
            $(name ).text( "Already accepted" );
        }
        return;
    })
}

/*
 * Function remove a teacher from the current view because a student chose to
 * decline him/her
 */
function decline(id){
    carousel = $("#"+id).parent().children('.carousel-item').first();
    if(carousel.attr("id") == id){
        carousel = $("#"+id).parent().children('.carousel-item').last();
    }
    carousel.addClass("active");
    $("#"+id).remove();
}
