// code for demostrating Request Modue in Node .JS

var request = require('request');

request('https://google.com', function(error, response, body){
	if(!error && response.statusCode===200){
		console.log(body);
	}
});