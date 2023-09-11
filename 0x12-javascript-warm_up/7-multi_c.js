#!/usr/bin/node
const process = require('process');
const elements = process.argv;
const x = parseInt(elements[2]);

if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
