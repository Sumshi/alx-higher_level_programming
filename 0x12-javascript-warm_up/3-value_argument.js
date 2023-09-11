#!/usr/bin/node
// argv[0] and argv[1] are reserved

// import built-in module "process"
const process = require('process');
const elements = process.argv;
if (elements[2]) {
  console.log(elements[2]);
} else {
  console.log('No argument');
}
