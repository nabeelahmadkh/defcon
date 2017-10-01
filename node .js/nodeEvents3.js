// code for demostrating Events in Node .JS 
// this program is interlinked with nodeEvents2.js
// Exported Module from nodeEvents2.js program is utilized there. 
// 

var Resource = require('./nodeEvents2');

var r = new Resource(5);

console.log(' __6__ '); // just for showing the flow of the program.

r.on('start', function(){
	console.log("I have started");
});

console.log(' __7__ '); // just for showing the flow of the program.

r.on('data',function(d){
	console.log("I have received data "+d);
});

console.log(' __8__ '); // just for showing the flow of the program.

r.on('end',function(t){
	console.log("I am done with "+t+"data events");
});

console.log(' __9__ '); // just for showing the flow of the program.