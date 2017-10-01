// code for demostrating the function callback in Node.JS

var maxTime = 1000;

var evenDouble = function (v, callback) {
    var waitTime = Math.floor(Math.random() * (maxTime + 1))
    if (v % 2) {
        setTimeout(function () {
            callback(new Error("Odd Input"))
        }, waitTime);
    } else {
        setTimeout(function () {
            callback(null, v * 2, waitTime);
        }, waitTime);
    }
};

var handleResults = function (err, results, time) {
    if (err) {
        console.log("Error:" + err.message);
    } else {
        console.log("The results are:" + results + "(" + time + "ms)");
    }
};

evenDouble(2, handleResults); // Second parameter is the callback function so once the function is complete then callback function can be called. 
evenDouble(3, handleResults); // the code continue to run, does not wait for the callback function to execute 

console.log("----");
