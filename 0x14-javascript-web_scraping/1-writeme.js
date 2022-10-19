#!/usr/bin/node
/**
 * Script that writes a string to a file
 */

const process = require('process');
const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', err => {
    if (err) {
        console.log(err);
    }
});
