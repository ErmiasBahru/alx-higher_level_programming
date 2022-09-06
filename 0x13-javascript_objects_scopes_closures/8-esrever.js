#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  while (list.length) {
    newList.push(list.pop());
  }
  return newList;
};
