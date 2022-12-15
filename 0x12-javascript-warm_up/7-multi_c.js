#!/usr/bin/node
const args = process.argv[2];
let i;
if (isNaN(args)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < args; i++) {
    console.log('C is fun');
  }
}
