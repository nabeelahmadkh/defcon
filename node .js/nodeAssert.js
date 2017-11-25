var assert = require('assert');
var fun = require('./nodeCallbackFunction')


assert.equal(fun.evenDoubleSync(2),4);
assert.throws(function(){
    fun.evenDoubleSync(3);
},/Odd/);

fun.evenDouble(2,function(err,results){
    assert.ifError(err);
    assert.equal(results,4,"Even Doubled failes on Even Number ");
})

fun.evenDouble(3, function(err,results){
    assert.notEqual(err,null);
})
