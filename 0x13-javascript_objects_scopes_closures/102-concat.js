#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: node 102-concat.js <fileA> <fileB> <fileC>');
  process.exit(1);
}

const [, , fileA, fileB, fileC] = process.argv;

fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    console.error(`Error reading ${fileA}: ${err.message}`);
    process.exit(1);
  }

  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) {
      console.error(`Error reading ${fileB}: ${err.message}`);
      process.exit(1);
    }

    const concatenatedData = dataA + '\n' + dataB;

    fs.writeFile(fileC, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${fileC}: ${err.message}`);
        process.exit(1);
      }

      console.log(`Concatenated ${fileA} and ${fileB} into ${fileC}`);
    });
  });
});
