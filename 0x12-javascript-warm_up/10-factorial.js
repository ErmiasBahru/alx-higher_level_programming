#!/usr/bin/node
const { argv } = require('process');

function factorial (num) {
  if (num === 0 || isNaN(num)) return (1);
  return (num * factorial(num - 1));
}

console.log(factorial(parseInt(argv[2])));
