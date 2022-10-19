#!/usr/bin/node
/**
 * Script that reads from a file
 */

const request = require('request');
const process = require('process');

const url = process.argv[2];

request.get(url, (err, resp) => {
    if (err === null) {
        console.log(`code: ${resp.statusCode}`);
    } else {
        console.log(err);
    }
});
