#!/usr/bin/node
const process = require('process');
const elements = process.argv;
if (!isNaN(elements[2])) {
  console.log('My number: ' + parseInt(elements[2]));
} else {
  console.log('Not a number');
}
