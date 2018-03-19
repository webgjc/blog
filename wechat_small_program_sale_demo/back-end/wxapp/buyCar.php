<?php
header("Content-Type: text/html; charset=utf-8");
$con = mysql_connect("localhost","root","gjc12345");
if (!$con){
    die('Could not connect: ' . mysql_error());
}else{
    mysql_select_db("wxapp", $con);
    $uid=$_GET['uid'];
    $sql="SELECT `buyCar` FROM `userInfo` WHERE ".$uid;
    $result = mysql_query($sql);
    $row=mysql_fetch_array($result);
    $re=array();
    $i=0;
    $tmparr=explode("|", $row['buyCar']);
    foreach($tmparr as $each){
        $sql="SELECT `name`,`imgurl` FROM `sellInfo` WHERE id=".$each[0];
        $result = mysql_query($sql);
        $arr=explode(",", $each);
        $res['id']=$i;
        $res['sid']=$arr[0];
        $res['type']=$arr[1];
        $res['price']=$arr[2];
        $res['num']=$arr[3];
        while($row=mysql_fetch_array($result)){
            $res['name']=$row['name'];
            $res['imgurl']=$row['imgurl'];
        }
        array_push($re, $res);
        $i++;
    }
    echo json_encode($re);
}