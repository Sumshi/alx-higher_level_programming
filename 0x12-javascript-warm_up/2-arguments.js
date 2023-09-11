#!/usr/bin/node

// accessing argv array
const elements = process.argv;
// check if no arguments are passed
if (elements.length === 2) {
  console.log('No argument');
} else if (elements.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
