<?php
  require_once("php_python.php"); //框架提供的程序脚本

  $p1 = 2;     
  $p2 = 3; 

  //"ppython"是框架"php_python.php"提供的函数，用来调用Python端服务
  //调用Python的testModule模块的add函数，并传递2个参数。
  $ret = ppython("testModule::add", $p1, $p2);

  echo "ret:".$ret;    //打印 5
?>