<?php
//获取私钥与加密后字符串进行解密
@session_start();
set_include_path('classes/phpseclib/');
include_once('Crypt/RSA.php');
$encrypted = $_POST['enc'];
$rsa = new Crypt_RSA();
$encrypted=pack('H*', $encrypted);
$rsa->loadKey($_SESSION['privatekey']);
$rsa->setEncryptionMode(CRYPT_RSA_ENCRYPTION_PKCS1);
$decrypted = $rsa->decrypt($encrypted);
echo $decrypted;