<?php
$con = mysql_connect("localhost","root","gjc12345");
if (!$con){
    die('Could not connect: ' . mysql_error());
}else{
    mysql_select_db("wxapp", $con);
    $result = mysql_query('SELECT * FROM sellInfo');
    $reslb = mysql_query('SELECT * FROM lbMain');
    $resArr['all']=array();
    $resArr['tj']=array();
    $resArr['lb']=array();
    while($row=mysql_fetch_array($result)){
        array_push($resArr['all'], array($row['id'],$row['name'],$row['imgurl'],$row['price']));
        if($row['tj']!=''){
            $resArr['tj'][explode(",", $row['tj'])[0]]=array($row['id'],explode(",", $row['tj'])[1]);
        }
    }
    while($row=mysql_fetch_array($reslb)){
        array_push($resArr['lb'], array($row['imgurl'],$row['pageid']));
    }
    echo json_encode($resArr);
}