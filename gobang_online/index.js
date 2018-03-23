var app=require('express')();
var http=require('http').Server(app);
var io=require('socket.io')(http);
var n=0;
var now=0;
app.get('/',function(req,res){
    res.sendFile(__dirname + '/index.html');
})
io.on('connection',function(socket) {
    n++;
    socket.on('disconnect',function(){
        n--;
        console.log('out');
    });
    socket.on('msg',function(info){
        console.log(now)
        if(info[2]!=now && n>=2){
            io.emit('message',{for:info})
            now=info[2];
        }
    })
});
http.listen(3000,function(){
    console.log('start')
})