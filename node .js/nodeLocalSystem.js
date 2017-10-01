// code for demostrating the Local System in Node.JS

process.stdin.resume();	// to avaoid automatic pausing of sts input stream.
process.stdin.setEncoding('utf8');

process.stdin.on('data',function(chunk){
	process.stdout.write('Data '+chunk);
});

process.stdin.on('end',function(){
	process.stderr.write('end');
});

console.log("the name of the process runnning is"+process.pid);