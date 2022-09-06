#!/usr/bin/node
const { argv } = require('process');

if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  const size = parseInt(argv[2]);
  const charArray = [];
  for (let i = 0; i < size; i++) {
    charArray.push('X');
  }
  for (let j = 0; j < size; j++) {
    console.log(charArray.join(''));
  }
}
