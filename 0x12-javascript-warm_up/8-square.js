#!/usr/bin/node
const args = process.argv[2];
let i;
let j = 0;
let r = '';
if (isNaN(args)) {
  console.log('Missing size');
} else {
  for (i = j; i < args; i++) {
    for (j < i; j < args; j++) r += 'X';
    console.log(r);
  }
}
