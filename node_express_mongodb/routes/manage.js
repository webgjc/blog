var express = require('express');
var router = express.Router();
var RetInfo = require("../common/retinfo");

var Mongo = require("../common/mongodb");
DB_POSTS = new Mongo("test_database","posts");

router.get("/",function(req, res, next){
    DB_POSTS.fetch({}).then((data)=>{
        return res.send(data);
    },(err)=>{
        return res.send(RetInfo.error(err.message));
    });
})

.post("/",function(req, res, next){
    DB_POSTS.save(req.body).then((data)=>{
        return res.send(RetInfo.success());
    },(err)=>{
        return res.send(RetInfo.error(err.message));
    });
})

.delete("/",function(req, res, next){
    data={"_id":req.body.id}
    DB_POSTS.delete(data).then((data)=>{
        return res.send(data)
    },(err)=>{
        return res.send(RetInfo.error(err.message))
    });
})

.put("/",function(req, res, next){
    const params = req.body;
    DB_POSTS.update({"_id":params.id},params).then((data)=>{
        return res.send(RetInfo.success());
    },(err)=>{
        return res.send(RetInfo.error(err.message));
    })
})

module.exports = router;
