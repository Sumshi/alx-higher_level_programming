// adds the class red to the header element on click

$(document).ready(function () {
    $('#red_header').click(function () {
        $("header").addClass("red");
    });
});
