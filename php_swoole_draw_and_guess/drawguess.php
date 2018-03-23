<?php
$table = new swoole_table(1024);
$table->column('fd', swoole_table::TYPE_INT);
$table->create();
$server = new swoole_websocket_server("0.0.0.0", 9501);
$server->table = $table;
$anstr="苹果,李子,梨子,榴莲,香蕉,橙子,番茄,柿子,葡萄,水蜜桃,核桃,哈密瓜,西瓜,菠萝,蓝莓,草莓,释迦,杨桃,椰子,板栗,樱桃,荔枝,龙眼,青梅,山楂,柠檬,金桔,芒果,坚果,胡桃,枇杷";
$ansarr=split(",", $anstr);
$ran=rand(0,count($ansarr));
$ans=$ansarr[$ran];
$startGame=new swoole_atomic(0);
$players=new swoole_atomic(999);
$k=new swoole_atomic(0);
$server->on('open', function($server, $req) {
    global $ans,$players,$startGame;
    $server->table->set($req->fd, array('fd' => $req->fd));
    if(count($server->table)==1){
        $data=json_encode(array("start"=>"-2","data"));
        $server->push($req->fd,$data);
    }
    if(count($server->table)==$players->get()){
        if($startGame->get()==0){
            $startGame->set(1);
            foreach ($server->table as $u) {
                if($u['fd']==$req->fd){
                    $data=json_encode(array("start"=>"-1","draw"=>"1","ans"=>$ans));
                    $server->push($u['fd'],$data);
                }else{
                    $data=json_encode(array("start"=>"-1","draw"=>"0"));
                    $server->push($u['fd'],$data);
                }
            }
        }
    }
});

$server->on('message', function($server, $frame) {
    //$server->push($frame->fd, $frame->data);
    global $ans,$ansarr,$players,$k;
    $getdata=json_decode($frame->data);
    if($getdata->start==-4){
        $ran=rand(0,count($ansarr));
        $ans=$ansarr[$ran];
        $i=0;
        foreach($server->table as $u) {
            if($i<$k->get()){
                $i++;
            }else{
                $player=$u["fd"];
                $k->set(($k->get()+1)%$players->get());
                break;
            }
        }
        foreach ($server->table as $u) {
                if($u['fd']==$player){
                    $data=json_encode(array("start"=>"-1","draw"=>"1","ans"=>$ans));
                    $server->push($u['fd'],$data);
                }else{
                    $data=json_encode(array("start"=>"-1","draw"=>"0"));
                    $server->push($u['fd'],$data);
                }
            }
    }
    if($getdata->start==-3){
        $players->set(intval($getdata->players));
    }else{
        if($getdata->start==6){
            echo $getdata->answer;
        }
        if($getdata->start==6 && $getdata->answer==$ans){
            foreach ($server->table as $u) {
                $res=array("start"=>"6","win"=>$frame->fd);
                $server->push($u['fd'], json_encode($res));//消息广播给所有客户端    
            }  
            $ran=rand(0,count($ansarr));
            $ans=$ansarr[$ran];
            $i=0;
            foreach($server->table as $u) {
                if($i<$k->get()){
                    $i++;
                }else{
                    $player=$u["fd"];
                    $k->set(($k->get()+1)%$players->get());
                    break;
                }
            }
            foreach ($server->table as $u) {
                if($u['fd']==$player){
                    $data=json_encode(array("start"=>"-1","draw"=>"1","ans"=>$ans));
                    $server->push($u['fd'],$data);
                }else{
                    $data=json_encode(array("start"=>"-1","draw"=>"0"));
                    $server->push($u['fd'],$data);
                }
            }
        }else{
            foreach ($server->table as $u) {
                $server->push($u['fd'], $frame->data);//消息广播给所有客户端
            }     
        }
    }
});

$server->on('close', function($server, $fd) {
    echo "client-{$fd} is closed\n"; 
    global $startGame;
    $server->table->del($fd);
    if(count($server->table)==1){
        $startGame->set(0);
    }
});

$server->start();