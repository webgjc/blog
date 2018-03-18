<?php
//wsdl地址
$url="wsdl地址";
//出现类似于SOAP-ERROR: Parsing WSDL: Couldn't load from的错误时加上下面这行
libxml_disable_entity_loader(false);
//调用SoapClient对象
$client=new SoapClient($url);
//查看里面的函数数组
print_r($client->__getFunctions());
//构造header
$header = new SoapHeader('上面xml里的url','HeaderName',array('username'=>xxx,'password'=>xxx),true);
//设置header
$client->__setSoapHeaders($header);
//调用FuncName并传入数据
$return = $client->FuncName(array('neededData'=>xxx));
print_r($return);