// code for demostrating Events in Node .JS 
// Events are an alternative to Callback with some additional features.

var EventEmitter = require('events').EventEmitter;

function getResource(c){
	var e = new EventEmitter(); // new object for creating the events.
	console.log(' __1__ '); // just for showing the flow of the program.
	process.nextTick(function(){
		var count = 0;
		console.log(' __2__ '); // just for showing the flow of the program.
		e.emit('start');
		var t = setInterval(function(){
			e.emit('data',++count);
			console.log(' __3__ '); // just for showing the flow of the program.
			if(count === c){
				e.emit('end',count);
				console.log(' __4__ '); // just for showing the flow of the program.
				clearInterval(t); // infinite loop is going to run if we dont clear the interval.
			}
		},10);
	});
	console.log(' __5__ ');
	return(e);
};

var r = getResource(5);

console.log(' __6__ ');

r.on('start', function(){
	console.log("I have started");
});

console.log(' __7__ ');

r.on('data',function(d){
	console.log("I have received data "+d);
});

console.log(' __8__ ');

r.on('end',function(t){
	console.log("I am done with "+t+"data events");
});

console.log(' __9__ ');