var express = require('express');
var router = express.Router();
var RetInfo = require("../common/retinfo");

/* GET users listing. */
router.get('/login', function(req, res, next) {
    username = req.query.username;
    password = req.query.password;
    
    if(!username || !password) return res.json(RetInfo.error("lack of params"));

    if(username == "admin" && password == "admin"){
        
        req.session.regenerate(function(err) {
            if(err) return res.json(RetInfo.error("login error"));
            req.session.loginUser = username;
            return res.json(RetInfo.success());
        });

    }else{
        return res.json(RetInfo.error("username or password error"));
    }
});

router.get("/loginout", function(req, res, next) {
    req.session.destroy(function(err) {
        if(err) return res.json(RetInfo.error("login out error"));
        return res.json(RetInfo.success());
    });
})

module.exports = router;
