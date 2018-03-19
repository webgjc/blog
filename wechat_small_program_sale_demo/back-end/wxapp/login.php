<?php
$con = mysql_connect("localhost","root","gjc12345");
if (!$con){
    die('Could not connect: ' . mysql_error());
}else{
    mysql_select_db("wxapp", $con);
    $code=$_GET['code'];
    $username=$_GET['username'];
    $gender=$_GET['gender'];
    $logourl=$_GET['logourl'];
    $url="https://api.weixin.qq.com/sns/jscode2session?appid=wxdaee6e919b1b752d&secret=898c5ddcdcc5f4a2efafc3dbdaecbc53&js_code=".$code."&grant_type=authorization_code";
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    $res = curl_exec($ch);
    curl_close($ch);
    $result=json_decode($res);
    $openid=$result->openid;
    $result = mysql_query('SELECT * FROM userInfo WHERE openid="'.$openid.'"');
    $row = mysql_fetch_array($result);
    if(!$row){
        $sql='INSERT INTO userInfo (openid,gender,username,logourl) VALUES ("'.$openid.'", '.$gender.', "'.$username.'","'.$logourl.'")'; 
        $insertRes=mysql_query($sql);
        if($insertRes){
            $re['code']=1;
            $re['id']=mysql_insert_id();
            echo json_encode($re);
        }else{
            $re['code']=0;
            echo json_encode($re);
        }
    }else{
        $re['code']=1;
        $re['id']=$row['id'];
        echo json_encode($re);
    }
}