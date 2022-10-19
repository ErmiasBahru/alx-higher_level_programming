#!/usr/bin/node
/**
 * Script that gets the contents of
 * a webpage and stores it in a file
 */
const request = require('request');
const process = require('process');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (err, _resp, body) => {
    if (err === null) {
        fs.writeFile(filePath, body, 'utf-8', fileError => {
            if (fileError !== null) {
                console.log(fileError);
            }
        });
    } else {
        console.log(err);
    }
});
