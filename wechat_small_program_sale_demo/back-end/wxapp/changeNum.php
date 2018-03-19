<?php
$con = mysql_connect("localhost","root","gjc12345");
if (!$con){
    die('Could not connect: ' . mysql_error());
}else{
    mysql_select_db("wxapp", $con);
    $id=$_GET['id'];
    $uid=$_GET['uid'];
    $num=$_GET['num'];
    $sql="SELECT `buyCar` FROM `userInfo` WHERE id=".$uid;
    $result = mysql_query($sql);
    $row=mysql_fetch_array($result);
    $arr=explode("|", $row['buyCar']);
    $Narr=explode(",", $arr[$id]);
    $Narr[3]=$num;
    if($num==0){
        $arr[$id]='';
    }else{
        $arr[$id]=$Narr[0].",".$Narr[1].",".$Narr[2].",".$Narr[3];
    }
    $str=$arr[0];
    for($j=1;$j<count($arr);$j++){
        if($arr[$j]!=''){
            $str=$str."|".$arr[$j];
        }
    }
    if($arr[0]==''){
        $str=substr($str,1);
    }
    $sql="UPDATE `userInfo` SET `buyCar` = '".$str."' WHERE id=".$uid;
    if(mysql_query($sql)){
        if($num==0){
            echo json_encode(array($id));
            return;
        }
        echo 1;
    }else{
        echo 0;
    }
}