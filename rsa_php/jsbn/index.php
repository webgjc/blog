<?php
@session_start();
$path = 'phpseclib';
set_include_path(get_include_path() . PATH_SEPARATOR . $path);
include_once('Crypt/RSA.php');

$plaintext = 'test';
var_dump($plaintext);

if (isset($_GET['enc'])) {
    $encrypted = $_GET['enc'];
    var_dump($_SESSION['privatekey']);
    $rsa = new Crypt_RSA();
    $encrypted=pack('H*', $encrypted);
    $rsa->loadKey($_SESSION['privatekey']);
    $rsa->setEncryptionMode(CRYPT_RSA_ENCRYPTION_PKCS1);
    $decrypted = $rsa->decrypt($encrypted);
    var_dump($decrypted);
    var_dump($plaintext == $decrypted);
    return;
}

$rsa = new Crypt_RSA();
$rsa->setPrivateKeyFormat(CRYPT_RSA_PRIVATE_FORMAT_PKCS1);
$rsa->setPublicKeyFormat(CRYPT_RSA_PUBLIC_FORMAT_RAW);

$key = $rsa->createKey(1024);
var_dump($key);
// return;

// $publickey = $key['publickey'];
$privatekey = $key['privatekey'];
$_SESSION['privatekey'] = $privatekey;

// $rsa = new Crypt_RSA();
// $rsa->loadKey($publickey);
// $rsa->setEncryptionMode(CRYPT_RSA_ENCRYPTION_PKCS1);
// $encrypted = bin2hex($rsa->encrypt($plaintext));
// var_dump($encrypted);

// $rsa = new Crypt_RSA();
// $rsa->loadKey($privatekey);
// $raw = $rsa->getPublicKey(CRYPT_RSA_PUBLIC_FORMAT_RAW);
// $publickey = $raw['n']->toHex();
$publickey = $key['publickey']['n']->toHex();
var_dump($publickey);

// $rsa = new Crypt_RSA();
// $encrypted=pack('H*', $encrypted);
// $rsa->loadKey($privatekey);
// $rsa->setEncryptionMode(CRYPT_RSA_ENCRYPTION_PKCS1);
// $decrypted = $rsa->decrypt($encrypted);
// var_dump($decrypted);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>test</title>
</head>
<body>
<div id="encrypted"></div>
<div id="decrypted"></div>
<script src="//cdn.bootcss.com/jquery/3.1.0/jquery.min.js"></script>
<script language="JavaScript" type="text/javascript" src="jsbn.js"></script>
<script language="JavaScript" type="text/javascript" src="prng4.js"></script>
<script language="JavaScript" type="text/javascript" src="rng.js"></script>
<script language="JavaScript" type="text/javascript" src="rsa.js"></script>
<script type="text/javascript">
var publickey = "<?=$publickey?>";
var rsakey = new RSAKey();
rsakey.setPublic(publickey, "10001");
var enc = rsakey.encrypt('<?=$plaintext?>');
$('#encrypted').html(enc);
$.get('index.php?enc='+enc, function(data) {
    $('#decrypted').html(data);
});
</script>
</body>
</html>
