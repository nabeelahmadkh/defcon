var express = require('express');
var firebase = require('firebase');

// Firebase Configuration
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
 
// Ref to Firebase Database created
var postsRef = firebase.database().ref('blogPost');

var app = express();

var port = 8080;

// Create a Router 
var bookRouter = express.Router();
bookRouter.route('/books') // books route
	.get(function(req,res){
		//var responseJson = {hello: "Welcome to API"};
		//res.json(responseJson);

		// listenign to value event of FireBase which will get all the data from the Firebase Database
		// and displaying the response intially.
		
		var query = req.query; // this will contain a query send from the browser.

		// Firebase Function for getting the value and returning it in the response.
		postsRef.on('value',function(snap){
			// printing the data in the console retrieved from the Firebase
			console.log('value',snap.val());
			res.json(snap.val());
		},function(err){
			// printing the error in Firebase
			console.log('Error!!!');
			console.log(err)
		});	
	});

// Creating a base routing path, you can see in the next block we are using /api as our base for the call 
app.get('/', function(request, response){
	response.send("hello");
});

app.use('/api',bookRouter); // now books will be accesible through /api/books link, as the bankRouter is using /api as its base

/*
app.get('/books', function(request, response){
	response.send("hello books");
});
*/

app.listen(port, function(err){
	console.log("server running on port"+port);
});