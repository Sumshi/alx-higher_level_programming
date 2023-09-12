#!/usr/bin/node
// Import the 'list' array from the file 100-data.js
const list = require('./100-data').list;

// Use the 'map' method to create a new array with values multiplied by their indices
const newList = list.map((value, index) => value * index);

// Print both the initial list and the new list
console.log(list);
console.log(newList);