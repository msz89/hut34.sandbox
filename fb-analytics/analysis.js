var fs = require('fs')
var Graph = require("...");

fs.readFile("fb.json", 'utf8', function (err,data){
	if (err) {
		return console.log(err);
	} 

	var set = JSON.parse(data).cryptobot
	var arrx = []
	var arry = []
	for (n in set){
		if (set[n].ticker == " BTC"){
			arrx.push(set[n].timestamp);
			arry.push(set[n].price);
		}
	}
	var chart = {
		x: arrx,
		y: arry,
		type: "scatter"
	}
	console.log(chart)
})

