#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import urllib2
import time
import json
import requests
reload(sys)
sys.setdefaultencoding('utf-8')


CORPID = "ww28670d7bb774bf0f"
SECRET = "61MCy18czLucTpwGh9l_tLov-HHqs8EdhmtZpv9Fr4A"
BASEURL = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={0}&corpsecret={1}'.format(CORPID, SECRET)
URL = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s"


class Token(object):
    # get token
    def __init__(self):
        self.expire_time = sys.maxint
    def get_token(self):
        if self.expire_time > time.time():
            request = urllib2.Request(BASEURL)
            response = urllib2.urlopen(request)
            result_string = response.read().strip()
            result_json = json.loads(result_string)
            self.expire_time = time.time() + result_json['expires_in']
            self.access_token = result_json['access_token']
        return self.access_token


def send_message(content):
    team_token = Token().get_token()
    url = URL % (team_token)
    wechat_json = {
        "toparty": "1|2",
        "msgtype": "text",
        "agentid": "1000002",
        "text": {
            "content": "jenkins执行结果：\n{0}".format(content)
        },
        "safe": "0"
    }
    response = requests.post(url, data=json.dumps(wechat_json, False,False))
    print response.json()


if __name__ == '__main__':
    send_message("jenkins任务构建失败")