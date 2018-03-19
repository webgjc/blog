<?php
$con = mysql_connect("localhost","root","gjc12345");
if (!$con){
    die('Could not connect: ' . mysql_error());
}else{
    mysql_select_db("wxapp", $con);
    $id=$_GET['id'];
    $sql='SELECT * FROM userInfo WHERE id="'.$id.'"';
    $result = mysql_query($sql);
    $row = mysql_fetch_array($result);
    echo json_encode($row);
}