/**
 * Script that fetches and lists the title for all movies
 * by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
 */
$.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: result => {
        const movies = result.results
        $.each(movies, (_index, movie) => {
            $('UL#list_movies').append('<li>' + movie.title + '</li>');
        });
    }
});
