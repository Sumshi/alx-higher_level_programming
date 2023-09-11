#!/usr/bin/node
// finds factorial
const process = require('process');
const arg1 = parseInt(process.argv[2]);
function factorial (n) {
  if (n === 0) {
    return 1;
  } else if (isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(arg1));
