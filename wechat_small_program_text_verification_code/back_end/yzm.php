<?php
include('phpqrcode/qrlib.php');
include('config.php'); 
#默认同一目录下
$tempDir = EXAMPLE_TMP_SERVERPATH; 
$a=$_GET['data'];
#如果获取到数字，则产生联系人名片二维码，否则是一般的文字二维码
#返回base64编码的图片
if(!is_numeric($a)){
    QRcode::png($a,$tempDir.'test.png',QR_ECLEVEL_L, 10);
    $str = file_get_contents($tempDir.'test.png');
    echo "data:image/png;base64,".base64_encode($str);
    //echo $tempDir.'test.png';
}else{
    $name = ''; 
    $phone = $a;
    $codeContents  = 'BEGIN:VCARD'."\n"; 
    $codeContents .= 'FN:'.$name."\n"; 
    $codeContents .= 'TEL;WORK;VOICE:'.$phone."\n"; 
    $codeContents .= 'END:VCARD'; 
    QRcode::png($codeContents, $tempDir.'test.png', QR_ECLEVEL_L, 10); 
    $str = file_get_contents($tempDir.'test.png');
    echo "data:image/png;base64,".base64_encode($str);
}