module.exports = {
    response : function(sts,msg) {
        return {"sts":sts,"msg":msg}
    },
    success : function() {
        return this.response(1,"success")
    },
    error : function(msg) {
        return this.response(-1,msg)
    },
    dberr : function(msg) {
        return this.response(-1,"db error");
    }
}