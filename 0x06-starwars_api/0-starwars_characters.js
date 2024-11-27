#!/usr/bin/env node
const request = require('request-promise')
const id = process.argv[2]
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`

async function getcharacter(endpoint){
	return request(endpoint, (err, res, body) => {
		if(err) {
			console.log(err)
		}
		obj = JSON.parse(body)
		console.log(obj['name'])
	})
}
async function getapilist(url){
	return request(url, (err, res, body) => {
		if (err){
			console.log(err)
		}
	})
}

async function myfunc(){
	const ans = await getapilist(url)
	apilist = JSON.parse(ans)['characters']
	for (ele of apilist) {
		await getcharacter(ele)
	};
}

myfunc()

// Luke Skywalker
// C-3PO
// R2-D2
// Darth Vader
// Leia Organa
// Obi-Wan Kenobi
// Chewbacca
// Han Solo
// Jabba Desilijic Tiure
// Wedge Antilles
// Yoda
// Palpatine
// Boba Fett
// Lando Calrissian
// Ackbar
// Mon Mothma
// Arvel Crynyd
// Wicket Systri Warrick
// Nien Nunb
// Bib Fortuna