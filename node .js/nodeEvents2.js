// code for demostrating Events in Node .JS 
// this program is interlinked with nodeEvents3.js
// Exported Module from this program is utilized there. 
// 

var util = require('util');
var EventEmitter = require('events').EventEmitter;

function getResource(c){
	var e = this;	// since EventEmitter class is already inherited into getRource, therefore we are using self object 

	console.log(' __1__ ');	// just for showing the flow of the program.
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
				clearInterval(t); // infenite loop is going to run if we dont clear the interval.
			}
		},10);
	});
	console.log(' __5__ '); // just for showing the flow of the program.
	return(e);
};

util.inherits(getResource, EventEmitter); // EventEmitter class is inherited into getResource 

module.exports = getResource;