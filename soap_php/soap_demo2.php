<?php
//用curl带着post包和header去获取数据
function getData($soap_request){
      //构造头信息，和第一种方法的header不一样，具体查看webservice说明。
      $header = array(
          "Content-type: application/soap+xml; charset=utf-8",
          "Host: xxx.xxx.xxx.xxx",
          "Content-length: ".strlen($soap_request),
        );
      $soap_do = curl_init();
      curl_setopt($soap_do, CURLOPT_URL, "wsdl地址");
      curl_setopt($soap_do, CURLOPT_RETURNTRANSFER, true );
      curl_setopt($soap_do, CURLOPT_POST,           true );
      curl_setopt($soap_do, CURLOPT_POSTFIELDS,     $soap_request);
      curl_setopt($soap_do, CURLOPT_HTTPHEADER,     $header);
      $data = curl_exec($soap_do);
      return $data;
}
//处理得到的xml数据
function handData($result,$parentNode,$childNode){
      $xml=simplexml_load_string($result);
      $result = $xml->children('http://www.w3.org/2003/05/soap-envelope')
        ->children('url')
        ->$parentNode
        ->$childNode;
      return $result;
}
//使用方法
//下面是上面xml的字符形式，将需要传入的数据直接写成标签到xml字符里
$soap_request = "<?xml version......";
$return = $this->getData($soap_request);
//后面两个参数为返回xml的body内的两个标签名
$result = $this->handData($return,FuncName,returnData);