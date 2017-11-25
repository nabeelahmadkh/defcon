var http = require('http');

var server = http.createServer(function(req, res){
	res.writeHead(200, {'content-type':'text/plain'});
	res.end("hello");
});

server.listen(8081);
console.log('server running');