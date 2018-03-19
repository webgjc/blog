<?php
$con = mysql_connect("localhost","root","gjc12345");
if (!$con){
    die('Could not connect: ' . mysql_error());
}else{
    mysql_select_db("wxapp", $con);
    $id=$_GET['uid'];
    $sql='SELECT * FROM orderDetail WHERE uid="'.$id.'"';
    $result = mysql_query($sql);
    $res=array();
    while($row=mysql_fetch_array($result)){
        array_unshift($res, $row);
    }
    echo json_encode($res);
}