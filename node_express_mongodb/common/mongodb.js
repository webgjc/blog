//use for mongodb database 

var MongoClient = require('mongodb').MongoClient;

function Mongodb(dbName, colName){

    this.dbName = dbName;
    this.colName = colName;
    this.url = 'mongodb://localhost:27017/';

    this.fetch = function(params){
        var that = this;
        return new Promise(function(resolve, reject, notufy) {
            MongoClient.connect(that.url, function(err, db){
                if(err) reject(err);
                var dbo = db.db(that.dbName);
                dbo.collection(that.colName).find(params).toArray(function(err, res){
                    if(err) reject(err);
                    resolve(res);
                    db.close();
                });
            });
        });
    };

    this.save = function(params){
        var that = this;
        return new Promise(function(resolve, reject, notufy){
            MongoClient.connect(that.url, function(err, db){
                if(err) reject(err);
                var dbo = db.db(that.dbName);
                dbo.collection(that.colName).insertOne(params, function(err, res){
                    if(err) reject(err);
                    resolve(res);
                    db.close();
                });
            });
        });
    };

    this.delete = function(params){
        var that = this;
        return new Promise(function(resolve, reject, notufy){
            MongoClient.connect(that.url, function(err, db){
                if(err) reject(err);
                var dbo = db.db(that.dbName);
                dbo.collection(that.colName).deleteOne(params, function(err, res){
                    if(err) reject(err);
                    resolve(res);
                    db.close();
                });
            });
        });
    }

    this.update = function(whparams,params){
        var that = this;
        return new Promise(function(resolve, reject, notufy){
            MongoClient.connect(that.url, function(err, db){
                if(err) reject(err);
                var dbo = db.db(that.dbName);
                dbo.collection(that.colName).updateOne(whparams, {$set:params}, function(err, res){
                    if(err) reject(err);
                    resolve(res);
                    db.close();
                });
            });
        });
    }
}

module.exports = Mongodb;