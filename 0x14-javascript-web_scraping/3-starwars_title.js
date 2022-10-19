#!/usr/bin/node
/**
 * Script that prints the title of a Star Wars movie
 * where the episode number matches a given integer
 */
const request = require('request');
const process = require('process');

const episodNumber = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${episodNumber}`;

request.get(url, (err, _resp, body) => {
    if (err === null) {
        const data = JSON.parse(body);
        console.log(data.title);
    } else {
        console.log(err);
    }
});
