var http = require('http');
var socketio = require('socket.io');
var fs = require('fs');

var handler = function(req, res){
	fs.readFile(__dirname + '/index.html',function(err,data){
		console.log(' __2__ ');
		if(err){
			res.writeHead(500);
			console.log('__6__');
			return res.end('error loading');
		}else{
			res.writeHead(200);
			console.log('__7__');
			res.end(data);
		}
	});
};

var app = http.createServer(handler);
var io = socketio.listen(app);
console.log(' __3__ ');

io.sockets.on('connection',function(socket){
	setInterval(function(){
		console.log(' __5__ ');
		var timeStamp = Date.now();
		console.log('emitted'+timeStamp);
		socket.emit('timer',timeStamp);
	},4000);
	socket.on('submit',function(data){
		console.log('submitted'+data);
	});
});

app.listen(8080);
console.log('server running');
console.log(' __4__ ');