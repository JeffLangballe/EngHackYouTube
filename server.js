var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var methodOverride = require('method-override');

var db = require('./config/db');
var port = process.env.port || 8080;

//mongoose.connect(db.url);

//app.use(bodyParser.json);     // TODO: fix this breaking the application 
app.use(express.static(__dirname + '/public'));

// Load the routes
require('./app/routes')(app);

app.listen(port);
console.log('Server started on ' + port);
module.exports = app;