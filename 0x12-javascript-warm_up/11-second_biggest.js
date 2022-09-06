#!/usr/bin/node
const { argv } = require('process');

if (argv.length <= 3) {
  console.log(0);
} else {
  let newArgv = argv.slice(2, argv.length);
  newArgv = newArgv.map((value) => parseInt(value));
  newArgv.sort((a, b) => b - a);
  console.log(newArgv[1]);
}
