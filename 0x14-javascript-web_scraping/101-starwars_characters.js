#!/usr/bin/node
/**
 * Script that prints all characters of a Star Wars movie
 */

const request = require('request');
const process = require('process');
const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

function characterRequest(characterUrl) {
    return new Promise((resolve, reject) => {
        request.get(characterUrl, (err, _resp, body) => {
            if (err !== null) {
                reject(err);
            }
            resolve(body);
        });
    });
}

request.get(url, (err, _resp, body) => {
    if (err === null) {
        const film = JSON.parse(body);
        const characters = film.characters;
        characters.forEach((character) => {
            characterRequest(character).then((body) => {
                const characterInfo = JSON.parse(body);
                console.log(characterInfo.name);
            }).catch(err => console.log(err));
        });
    } else {
        console.log(err);
    }
});
