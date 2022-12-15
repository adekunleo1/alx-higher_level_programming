#!/usr/bin/node
const args = Math.floor(Number(process.argv[2]));
if (isNaN(args)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + args);
}
