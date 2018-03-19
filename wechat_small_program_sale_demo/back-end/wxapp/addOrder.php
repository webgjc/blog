<?php
$con = mysql_connect("localhost","root","gjc12345");
if (!$con){
    die('Could not connect: ' . mysql_error());
}else{
    mysql_select_db("wxapp", $con);
    $uid=$_GET['uid'];
    $con=$_GET['contain'];
    $price=$_GET['price'];
    $sid=$_GET['sid'];
    $time=date("Y-m-d H:i:s",time());
    $sql="SELECT * FROM `userInfo` WHERE id=".$uid;
    $result = mysql_query($sql);
    $row=mysql_fetch_array($result);
    $place=$row['address'];
    $phone=$row['phone'];
    $state=0;
    $sql='INSERT INTO `orderDetail` (uid,sid,place,phone,contain,price,state) VALUES ("'.$uid.'","'.$sid.'", "'.$place.'", "'.$phone.'","'.$con.'","'.$price.'",'.$state.')'; 
    if(mysql_query($sql)){
        echo 1;
    }else{
       die('Error: ' . mysql_error());
    }
}