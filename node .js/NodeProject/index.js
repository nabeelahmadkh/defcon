var express = require('express');

var app = express();

var port = 8080;

app.get('/', function(request, response){
	response.send("hello");
});


app.get('/books', function(request, response){
	response.send("hello books");
});

app.listen(port, function(err){
	console.log("server running on port"+port);
});