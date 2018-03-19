<?php
$con = mysql_connect("localhost","root","gjc12345");
if (!$con){
    die('Could not connect: ' . mysql_error());
}else{
    mysql_select_db("wxapp", $con);
    $sid=$_GET['sid'];
    $arr=explode(",", $sid);
    array_pop($arr);
    $sql='SELECT `id`,`name` FROM sellInfo WHERE id="'.$arr[0].'" ';
    for($i=1;$i<count($arr);$i++){
        $sql.=' or id="'.$arr[$i].'"';
    }
    $result = mysql_query($sql);
    $res=array();
    while($row=mysql_fetch_array($result)){
        array_push($res,$row);
    }
    echo json_encode($res);
}