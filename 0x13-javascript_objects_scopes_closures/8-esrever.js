#!/usr/bin/node
//  returns the reversed version of a list
exports.esrever = function (list) {
  // return list.reverse();
  let start = 0;
  let end = list.length - 1;

  while (start < end) {
    // swap the elements at start and end positions
    const temp = list[start];
    list[start] = list[end];
    list[end] = temp;

    start++;
    end--;
  }
  return list;
};
