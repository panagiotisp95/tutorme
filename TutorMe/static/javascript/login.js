/*
 * When the document is fully loaded the given text will start
 * typed using the typed function
 */
$(document).ready(function () {
    $(".animated-text").typed({
        strings: [
            "Are you a teacher?",
            "Are you a student?",
            "You are at the right place!"
        ],
        smartBackspace: true,
        typeSpeed: 50,
        loop: true,
        backSpeed: 50,
        backDelay: 50,
    });
});

/*
 * Function call fb attempt login
 */
function login(){
    attemptLogin('/tutorme/login/');
}
