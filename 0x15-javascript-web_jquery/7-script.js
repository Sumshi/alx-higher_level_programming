// fetches data from a url
$(document).ready(function () {
  // URL to fetch character data
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  // Perform an AJAX GET request to fetch the character data
  $.get(url, function (data) {
    // Extract the character name from the response
    const characterName = data.name;

    // Display the character name in the DIV#character element
    $('#character').text(characterName);
  });
});
