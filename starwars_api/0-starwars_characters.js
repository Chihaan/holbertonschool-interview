#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

function gatherName (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, function (error, reponse, body) {
      if (error) {
        reject(error);
        return;
      }
      const characterInfo = JSON.parse(body);
      resolve(characterInfo.name);
    });
  });
}

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const infos = JSON.parse(body);
  const characters = infos.characters;
  Promise.all(characters.map((characterUrl) => gatherName(characterUrl))).then((names) => {
    names.forEach((name) => console.log(name));
  }).catch((error) => console.error(error));
});
