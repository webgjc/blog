onmessage=function(e){
    function fb(n){
        if(n==1||n==2){
            return 1;
        }else{
            return fb(n-1)+fb(n-2);
        }
    }
    postMessage(fb(e.data));
}