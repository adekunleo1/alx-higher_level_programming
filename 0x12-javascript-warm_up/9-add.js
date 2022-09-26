#!/usr/bin/node
function add (a, b) {
  const result = a + b;
  return result;
}
const answer = add(Number(process.argv[2]), Number(process.argv[3]));
console.log(answer);
