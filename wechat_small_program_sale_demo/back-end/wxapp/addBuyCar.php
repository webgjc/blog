<?php
$con = mysql_connect("localhost","root","gjc12345");
if (!$con){
    die('Could not connect: ' . mysql_error());
}else{
    mysql_select_db("wxapp", $con);
    $id=$_GET['id'];
    $type=$_GET['val'];
    $price=$_GET['price'];
    $sql="SELECT `buyCar` FROM `userInfo` WHERE ".$id;
    $result = mysql_query($sql);
    $row=mysql_fetch_array($result);
    $f=$row['buyCar']==""?"":"|";
    $buyCar=$row['buyCar'].$f.$id.",".$type.",".$price.",1";
    $sql="UPDATE `userInfo` SET `buyCar`='".$buyCar."' WHERE ".$id;
    if(mysql_query($sql)){
        echo 1;
    }else{
        echo 0;
    }
}