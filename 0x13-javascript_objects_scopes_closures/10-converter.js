#!/usr/bin/node

exports.converter = function (base) {
  return value => value.toString(base);
};
