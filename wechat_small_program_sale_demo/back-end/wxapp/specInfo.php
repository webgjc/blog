<?php
$con = mysql_connect("localhost","root","gjc12345");
if (!$con){
    die('Could not connect: ' . mysql_error());
}else{
    mysql_select_db("wxapp", $con);
    $id=$_GET['id'];
    $sql='SELECT * FROM sellInfo WHERE id="'.$id.'"';
    $result = mysql_query($sql);
    $row=mysql_fetch_array($result);
    $sql='SELECT * FROM comment WHERE id="'.$id.'"';
    $result = mysql_query($sql);
    $comment=array();
    while($i=mysql_fetch_array($result)){
        array_unshift($comment, array($i['username'],$i['time'],$i['com']));
    }
    $res['comment']=$comment;
    $res['info']=$row;
    echo json_encode($res);
}