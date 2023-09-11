#!/usr/bin/node
function factorialIterative (n) {
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
}

// Example usage:
const result = factorialIterative(5); // Calculates 5!
console.log(result); // Output: 120
