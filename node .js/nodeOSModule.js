// code for demostrating OS module in Node .JS

var os = require("os");

var toMb = function(f){
	return(Math.round((f/1024/1024)*100)/100);
}

console.log(' ');
console.log('Host '+os.hostname());
console.log('ismn avg '+os.loadavg()[2]);
console.log(toMb(os.freemem())+' of '+toMb(os.totalmem())+' Mb Free');
