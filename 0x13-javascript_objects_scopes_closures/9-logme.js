#!/usr/bin/node

let trackLogs = 0;

exports.logMe = function (item) {
  console.log(`${trackLogs}: ${item}`);
  trackLogs++;
};
