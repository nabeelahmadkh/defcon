// Code for Nbroadcast Posts REST APIs
// Written by Nabeel Ahmad Khan
// Last edit on 25/12/2017


var express = require('express');
var firebase = require('firebase');

// Firebase Configuration can be pulled from Firebase Console
var config = {
	apiKey: "AIzaSyC-d8dYJrCubsmFdYn2FKDcq1jhwA9PE3I",
	authDomain: "blogproject-f3538.firebaseapp.com",
	databaseURL: "https://blogproject-f3538.firebaseio.com",
	storageBucket: "blogproject-f3538.appspot.com"
  };

// Initializing Firebase App
var defaultApp = firebase.initializeApp(config);
console.log("Firebase Connected");
console.log(defaultApp.name);

// Function for checking wheather the object has a value or not.
function isEmpty(obj) {
    // null and undefined are "empty"
    if (obj == null) return true;
 
    // Assume if it has a length property with a non-zero value
    // that that property is correct.
    if (obj.length && obj.length > 0)    return false;
    if (obj.length === 0)  return true;
 
    // Otherwise, does it have any properties of its own?
    // Note that this doesn't handle
    // toString and toValue enumeration bugs in IE < 9
    for (var key in obj) {
        if (hasOwnProperty.call(obj, key)) return false;
    }
 
    return true;
}
 
// Ref to Firebase Database created
var postsRef = firebase.database().ref('blogPost');

var app = express();

var port = 8080;

// Create a Router 
var postsRouter = express.Router();
postsRouter.route('/allposts') // books route
	.get(function(req,res){
		//var responseJson = {hello: "Welcome to API"};
		//res.json(responseJson);

		// listenign to value event of FireBase which will get all the data from the Firebase Database
		// and displaying the response intially.
		
		var query = req.query.post; // this will contain a query send from the browser. by using <server-address>/allposts/?post=search_term

		// If the user search for a post in the browser then If case will run
		if (!isEmpty(query)){ 
			childPostRef = postsRef.child(query)
			console.log("in the IF CASE")
			console.log(query)
			childPostRef.once('value',function(childSnap){
				console.log(childSnap.val());
				res.json(childSnap.val());
			},function(err){
				console.log(err);
				res.status(err);
			});
		}
		// This will run when the user runs <server-address>/allposts/
		else{
		// Firebase Function for getting the value and returning it in the response.
		// 'value' is the event that listens to any change in the Firebase Database 
			console.log("in the ELSE CASE")
			postsRef.once('value',function(snap){
				// printing the data in the console retrieved from the Firebase
				console.log(snap.val());
				res.json(snap.val());
			},function(err){
				// printing the error in Firebase
				console.log('Error!!!');
				console.log(err)
				res.status(err) // returning the error status to the web page
			});
		}	
	});



// Creating a base routing path, you can see in the next block we are using /api as our base for the call 
app.get('/', function(request, response){
	response.send("Welcome to Nbroadcast API");
});

// Default Path for using postsRouter
app.use('/',postsRouter); // now books will be accesible through /api/books link, as the bankRouter is using /api as its base


app.listen(port, function(err){
	console.log("server running on port"+port);
});