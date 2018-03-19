<?php
$con = mysql_connect("localhost","root","gjc12345");
if (!$con){
    die('Could not connect: ' . mysql_error());
}else{
    mysql_select_db("wxapp", $con);
    $id=$_GET['id'];
    $address=$_GET["address"];
    $phone=$_GET["phone"];
    $sql='UPDATE `userInfo` SET `address` = "'.$address.'", phone="'.$phone.'" WHERE id = '.$id.'';
    if(mysql_query($sql)){
        echo 1;
    }else{
        echo 0;
    }
}