<?php
header("Content-Type: text/html; charset=utf-8");

$username = "xxx";
$password = "xxx";

$cookie=dirname(__FILE__).'/cookie.txt';

#先访问一次获取参数lt
$ch = curl_init(); 
curl_setopt($ch, CURLOPT_URL, 'http://cas.hdu.edu.cn/cas/login'); 
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$res=curl_exec($ch);
curl_close($ch);
$preg = '|<input type="hidden" name="lt" value=[\"](.*?)[\"] />|U';
preg_match_all($preg, $res, $arr); 
$lt=$arr[1][0];

#登录，模拟他的post请求
$post_data=array(
    'encodedService'=>'http%3a%2f%2fi.hdu.edu.cn%2fdcp%2findex.jsp',
    'service'=>'http://i.hdu.edu.cn/dcp/index.jsp',
    'serviceName'=>'null',
    'loginErrCnt'=>'0',
    'username'=>$username,
    'password'=>md5($password),
    'lt'=>$lt
);
$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, "http://cas.hdu.edu.cn/cas/login");
curl_setopt($curl, CURLOPT_HEADER, 0);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
curl_setopt ($curl,CURLOPT_REFERER,'http://cas.hdu.edu.cn/cas/login');
curl_setopt($curl, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'); 
curl_setopt($curl, CURLOPT_POST, 1);//post方式提交 
curl_setopt($curl, CURLOPT_COOKIEJAR, $cookie);
curl_setopt($curl, CURLOPT_POSTFIELDS, http_build_query($post_data));//要提交的信息 
curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 3);       

#这里成功会返回一个window.location.href跳转
$res=curl_exec($curl);//执行cURL 
curl_close($curl);

#匹配跳转，也可以带cookie继续访问进去
preg_match_all('/window.location.href=[\"](.*)[\"]/i', $res, $results);
if(is_null($results[1][0])){
    echo "用户名密码错误";
}else{
    echo "已登录，可继续带cookie访问 ".$results[1][0];
}