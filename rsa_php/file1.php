<?php
//产生公钥与私钥
@session_start();
set_include_path('classes/phpseclib/');
include_once('Crypt/RSA.php');
$rsa = new Crypt_RSA();
$rsa->setPrivateKeyFormat(CRYPT_RSA_PRIVATE_FORMAT_PKCS1);
$rsa->setPublicKeyFormat(CRYPT_RSA_PUBLIC_FORMAT_RAW);
$key = $rsa->createKey(1024);
$privatekey = $key['privatekey'];
$_SESSION['privatekey'] = $privatekey;
$publickey = $key['publickey']['n']->toHex();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>test</title>
</head>
<body>
    <input type="text" placeholder="要加密字符串" id="str">
    <button id="sub">submit</button>
    <div id="encrypted"></div>
    <div id="decrypted"></div>
    <script src="//cdn.bootcss.com/jquery/3.1.0/jquery.min.js"></script>
    <script type="text/javascript" src="jsbn/jsbn.js"></script>
    <script type="text/javascript" src="jsbn/prng4.js"></script>
    <script type="text/javascript" src="jsbn/rng.js"></script>
    <script type="text/javascript" src="jsbn/rsa.js"></script>
    <script type="text/javascript">
    //js获得公钥进行加密
    var publickey = "<?=$publickey?>";
    var rsakey = new RSAKey();
    rsakey.setPublic(publickey, "10001");
    $("#sub").click(function(){
        var enc = rsakey.encrypt($("#str").val());
        $('#encrypted').html("加密后\n"+enc);
        $.post('file2.php', {enc: enc}, function(data) {
            $('#decrypted').html("解密后\n"+data);
        });
    });
    </script>
</body>
</html>