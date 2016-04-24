/**
 * Dependencies
 * */
 var pg = require('pg');


/**
 * PostgreSQL Config
 * */
 var HOST = "107.170.232.222";
 var PORT = 5432;
 var USER = "takecare_role";
 var PASSWORD = "takecare_pass";
 var DATABASE = "takecare";
 var CONNECTION_STRING = "postgres://" + USER + ":" + PASSWORD + "@" + HOST + "/" + DATABASE;
 

var insertPoint = function(lat, lng, comment, callback){
    var query = "INSERT INTO crowd_points(\"comment\",\"the_geom\") VALUES ('" + comment + "', ST_SetSRID(ST_MakePoint(" + lng + ", " + lat  + "),4326))";
    
    pg.connect(CONNECTION_STRING, function(err, client, done) {
        if(err) {
            return console.error('error fetching client from pool', err);
        }
        
        client.query(query, [], function(err, result) {
            done();     //call `done()` to release the client back to the pool
            callback(err,result);
        });
    });
};


var getAllPoints = function(callback){
    var query = "SELECT comment, ST_X(the_geom) as x, ST_Y(the_geom) as y FROM crowd_points";
    
    pg.connect(CONNECTION_STRING, function(err, client, done) {
        if(err) {
            return console.error('error fetching client from pool', err);
        }
        
        client.query(query, [], function(err, result) {
            done();     //call `done()` to release the client back to the pool
            callback(err,result);
        });
    });
};



var getIntersectionPoints = function(long, lat, long_x, lat_x, callback){
    getBounds(long,lat,long_x,lat_x, function(err, result){
        if(err){
            console.log("Error obteniendo los bounds");
        }
        
        var query = "SELECT * FROM crowd_points WHERE ST_Intersects( the_geom, '";
        query += result.rows[0].bounds;
        query += "'::geometry)";
        
        
        pg.connect(CONNECTION_STRING, function(err, client, done) {
            if(err) {
                return console.error('error fetching client from pool', err);
            }
            
            client.query(query, [], function(err, resultQuery) {
                done();     //call `done()` to release the client back to the pool
                callback(err,resultQuery);
            });
        });
    });
};



var getBounds = function(long, lat, long_x, lat_x, callback){
    /*    Creamos consulta  */
    var sql = "SELECT ST_AsText( ST_Envelope( ST_Collect(";
    
    //p1
    sql += "'POINT(" + long + " " + lat + ")'::geometry, ";
    //p2
    sql += "'POINT(" + long_x + " " + lat_x + ")'::geometry";
    sql += "))) as bounds";
    
    pg.connect(CONNECTION_STRING, function(err, client, done) {
        if(err) {
            return console.error('error fetching client from pool', err);
        }
        
        client.query(sql, [], function(err, result) {
            done();     //call `done()` to release the client back to the pool
            callback(err,result);
        });
    });
};


/**
 * DAO
 * */
module.exports = {
    insertPoint: insertPoint,
    getIntersectionPoints: getIntersectionPoints,
    getBounds: getBounds,
    getAllPoints: getAllPoints
};
