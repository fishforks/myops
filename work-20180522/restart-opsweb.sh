supervisorctl -c /home/xm/work/tmp/supervisord.conf stop opsweb
rm -rf /home/xm/work/tmp/opsweb.sock
supervisorctl -c /home/xm/work/tmp/supervisord.conf start opsweb
systemctl restart nginx
