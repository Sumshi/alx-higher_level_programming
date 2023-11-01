$(document).ready(function () {
    // URL to fetch movie data
    var url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

    // Perform an AJAX GET request to fetch the movie data
    $.get(url, function (data) {
        // Extract movie titles from the response
        var movies = data.results;
        var movieList = '';

        // Loop through the movies and create list items
        for (var i = 0; i < movies.length; i++) {
            movieList += '<li>' + movies[i].title + '</li>';
        }

        // Append the movie list to the UL#list_movies element
        $('#list_movies').html(movieList);
    });
});
