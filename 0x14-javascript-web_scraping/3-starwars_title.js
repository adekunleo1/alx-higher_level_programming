#!/usr/bin/node
const request = require('request');
let url = 'https://swapi-api.alx-tools.com/api/films/:id' + process.argv[2];
request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
