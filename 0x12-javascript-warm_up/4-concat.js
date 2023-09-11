#!/usr/bin/node
// argv[0] and argv[1] are reserved

// import built-in module "process" to use process
const process = require('process');
const elements = process.argv;
console.log(elements[2] + ' ' + 'is' + ' ' + elements[3]);
