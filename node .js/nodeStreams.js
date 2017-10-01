// code for demostrating the Input & Output Streams in Node.JS

var request = require('request');

var s = request('https://google.com');

s.on('data',function(chunk){
	console.log(">>Data is >>"+chunk);
});

s.on('end',function(){
	console.log(">>Done>>");
});


console.log("stdio is writable "+process.stdout.writable);
process.stdout.write("Hello");

request('https://google.com').pipe(process.stdout); // another way of printing the above statement, request is the read stream which is reading data and giving input to the pipe function which is taking this streamn and puching to the output stream process.stdout
