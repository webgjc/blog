<?php 
$con = mysql_connect("localhost","root","gjc12345");
if (!$con){
    die('Could not connect: ' . mysql_error());
}else{
    mysql_select_db("wxapp", $con);
    $data=$_GET['data'];
    $uid=$_GET['uid'];
    $oid=$_GET['oid'];
    $data=explode("|", $data);
    array_pop($data);
    $sql='SELECT `username` FROM userInfo WHERE id="'.$uid.'"';
    $result = mysql_query($sql);
    $row=mysql_fetch_array($result);
    foreach ($data as $i) {
        $item=explode("&", $i);
        $sql='INSERT INTO `comment` (id,uid,username,com) VALUES ("'.$item[0].'","'.$uid.'","'.$row["username"].'","'.$item[1].'")'; 
        if(!mysql_query($sql)){
           echo 0;
           return;
        }
    }
    $sql='UPDATE `orderDetail` SET `state` = 3 WHERE id = '.$oid.'';
    if(mysql_query($sql)){
        echo 1;
    }else{
        echo 0;
    }
}