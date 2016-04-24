/**
 * Module Dependencies
 * */
var express = require('express');
var app = express();
var http = require('http').Server(app);
var path = require('path');
var bodyParser = require('body-parser');
var io = require('socket.io')(http);
var pgrouting = require("./pgrouting.js");


app.use(bodyParser.json()); //json as param support
app.use(bodyParser.urlencoded({ extended: false })); //data as param support

app.use(express.static(path.join(__dirname, 'bootleaf'))); //Make resources public.. for... testing.... 

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

//
/**
 * 
 * Routers controllers
 * 
 * */
var apiRouter = require("./router/apiRouter.js");
app.use("/api/v1/", apiRouter);


io.on('connection', function(socket){
  
  pgrouting.getAllPoints(function(err, result){
    if(err){
      console.log("Error getting the data");
    }else{
      socket.emit("markers",result.rows);
    }
  });
  
  socket.on("addPoint", function(data){
    pgrouting.insertPoint(data.lat, data.lng, data.comment, function(err, result){
      if(err){
        console.log("Error en el query: ", err);
      }
    });
  });
  
});

/**
 * 
 * Service Configuration
 * 
 * */
app.set('port', process.env.PORT || 16502);


/**
 * 
 * Start
 * 
 * */
http.listen(app.get('port'), function(){
  console.log('Express server listening on port ' + app.get('port'));
});
