$(document).ready(function () {
    // URL to fetch the translation
    var url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

    // Perform an AJAX GET request to fetch the translation
    $.get(url, function (data) {
        // Display the translation in the DIV#hello element
        $('#hello').text(data.hello);
    });
});
