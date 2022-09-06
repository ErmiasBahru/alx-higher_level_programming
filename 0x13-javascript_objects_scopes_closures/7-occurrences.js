#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const filteredList = list.filter(item => item === searchElement);
  return filteredList.length;
};
