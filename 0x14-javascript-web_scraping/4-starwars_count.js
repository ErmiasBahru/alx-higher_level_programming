#!/usr/bin/node
/**
 * Script that prints the number of movies
 * where the character “Wedge Antilles” is present.
 */
const request = require('request');
const process = require('process');

const url = process.argv[2];

request.get(url, (err, _resp, body) => {
    if (err === null) {
        const data = JSON.parse(body);
        let films = data.results;
        films = films.filter(
            film => film.characters.find(
                character => character.match(/18/)
            )
        );
        console.log(films.length);
    } else {
        console.log(err);
    }
});
