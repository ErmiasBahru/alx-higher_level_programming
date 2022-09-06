#!/usr/bin/node
const { argv } = require('process');

const argvLength = argv.length - 2;
if (argvLength <= 0) {
  console.log('No argument');
} else if (argvLength === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
