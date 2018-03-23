#!/bin/sh
kill `lsof -t -i:9501`
sleep 2
php /home/swooleProject/drawguess.php
sleep 1
netstat -ntlp