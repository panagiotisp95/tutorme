$(document).ready(function() {

    $('.owl-carousel').owlCarousel({
    mouseDrag:false,
    loop:true,
    margin:2,
    nav:true,
    responsive:{
    0:{
    items:1
    },
    600:{
    items:1
    },
    1000:{
    items:3
    }
    }
    });
    
    $('.owl-prev').click(function() {
    $active = $('.owl-item .item.show');
    $('.owl-item .item.show').removeClass('show');
    $('.owl-item .item').removeClass('next');
    $('.owl-item .item').removeClass('prev');
    $active.addClass('next');
    if($active.is('.first')) {
    $('.owl-item .last').addClass('show');
    $('.first').addClass('next');
    $('.owl-item .last').parent().prev().children('.item').addClass('prev');
    }
    else {
    $active.parent().prev().children('.item').addClass('show');
    if($active.parent().prev().children('.item').is('.first')) {
    $('.owl-item .last').addClass('prev');
    }
    else {
    $('.owl-item .show').parent().prev().children('.item').addClass('prev');
    }
    }
    });
    
    $('.owl-next').click(function() {
    $active = $('.owl-item .item.show');
    $('.owl-item .item.show').removeClass('show');
    $('.owl-item .item').removeClass('next');
    $('.owl-item .item').removeClass('prev');
    $active.addClass('prev');
    if($active.is('.last')) {
    $('.owl-item .first').addClass('show');
    $('.owl-item .first').parent().next().children('.item').addClass('prev');
    }
    else {
    $active.parent().next().children('.item').addClass('show');
    if($active.parent().next().children('.item').is('.last')) {
    $('.owl-item .first').addClass('next');
    }
    else {
    $('.owl-item .show').parent().next().children('.item').addClass('next');
    }
    }
    });

    });

    $(document).ready(function(){

        $('.items').slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 3
        });
        });

$(document).ready(function(){
    /* 1. Visualizing things on Hover - See next part for action on click */
    $('#stars li').on('mouseover', function(){
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

    /* 2. Action to perform on click */
    $('#stars li').on('click', function(){
        var onStar = parseInt($(this).data('value'), 10); // The star currently selected
        var stars = $(this).parent().children('li.star');

        for (i = 0; i < stars.length; i++) {
            $(stars[i]).removeClass('selected');
        }

        for (i = 0; i < onStar; i++) {
            $(stars[i]).addClass('selected');
        }

        // JUST RESPONSE (Not needed)
        var ratingValue = parseInt($('#stars li.selected').last().data('value'), 10);
        var user = $("#stars").parent().parent().attr('class');
        console.log(user);
        console.log(ratingValue);
    });


});
