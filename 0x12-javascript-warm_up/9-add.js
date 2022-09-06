#!/usr/bin/node
const { argv } = require('process');

/**
 * add - adds two numbers
 * Return: sum of two numbers
 */
function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  return (a + b);
}

console.log(add(argv[2], argv[3]));
