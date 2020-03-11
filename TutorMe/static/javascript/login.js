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

function login(){
    attemptLogin('/tutorme/login/');
}
