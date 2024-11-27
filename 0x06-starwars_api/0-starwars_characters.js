#!/usr/bin/env node
const request = require('request-promise');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

async function getcharacter (endpoint) {
  return request(endpoint, (err, res, body) => {
    if (err) {
      console.log(err);
    }
    const obj = JSON.parse(body);
    console.log(obj.name);
  });
}
async function getapilist (url) {
  return request(url, (err, res, body) => {
    if (err) {
      console.log(err);
    }
  });
}

async function myfunc () {
  const ans = await getapilist(url);
  const apilist = JSON.parse(ans).characters;
  for (const ele of apilist) {
    await getcharacter(ele);
  }
}

myfunc();
