#!/bin/bash
num=`ps -ef | grep supervisord | wc -l`
if [ $num -ge 4 ];then
  ps -ef | grep supervisord | head -1|awk '{print $2}'|xargs kill -9
  /usr/bin/rm -rf /tmp/supervisor*
  /usr/bin/supervisord -c /home/xm/work/tmp/supervisord.conf
else
  /usr/bin/supervisord -c /home/xm/work/tmp/supervisord.conf
fi
