# coding: utf-8
import sys, os
import requests
import json
import traceback
import time
import Util

class QYWeixinMsg(object):
    __config = None
    access_token = None

    #### 实现单例
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            orig = super(QYWeixinMsg, cls)
            cls._instance = orig.__new__(cls)
            cls._instance.__init()
        return cls._instance

    #### 初始化函数，将在__new__方法后执行
    def __init(self):
        self.s = requests.session()
        #self.s.mount('https://', helpers.Ssl3HttpAdapter())
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }
        self.s.headers.update(headers)
        cfg = Util.file2dict(os.path.dirname(os.path.abspath(__file__)) + '/config/global.json')
        if cfg and cfg["QiYeWeiXin"]:
            self.__config = cfg["QiYeWeiXin"]
            self.__getToken()

    #### 获取token
    def __getToken(self):
        if not self.__config:
            return False
        
        para = dict(
            corpid=self.__config['corpid'],
            corpsecret=self.__config['corpsecret']
        )
        try:
            res = self.s.post(self.__config['login_url'], params=para)
            jt = json.loads(res.text)
            if jt.has_key('access_token'):
                self.access_token = jt['access_token']
            else:
                Util.echo("[Error] getToken %s" % res.text)
                self.access_token = None
                return False
        except Exception as exp:
            self.access_token = None
            Util.echo("[Error] __getToken(), " + repr(exp))
            traceback.print_exc()
            return False
        return True
    
    ## 发送消息
    def sendMsg(self, content, retry=2):
        if not isinstance(content, unicode):
            Util.echo(u"[Error] sendMsg content is not unicode")
            return False
        if content == "":
            Util.echo(u"[Error] sendMsg content is empty")
            return False
        if self.access_token is None:
            Util.echo(u"[Error] sendMsg(%s), access_token is not correct" % content)
            return False
        if retry <= 0:
            Util.echo(u"[Error] sendMsg retry end msg = %s" % content)
            return False
        para = dict(
            access_token = self.access_token,
        )
        data = {
            "touser": "@all",
            "toparty": "@all",
            "totag": "",
            "msgtype": "text",
            "agentid": self.__config['agentid'],
            "text": {"content": content},
            "safe": "0",
        }
        try:
            res = self.s.post(self.__config['send_url'], params=para,
                data=json.dumps(data, ensure_ascii=False).encode('utf-8'))
            jt = json.loads(res.text)
            if jt['errcode'] != 0:
                Util.echo(u"[Error] sendMsg result = %s, retry = %s" % (res.text, retry))
                time.sleep(10)
                if self.__getToken():
                    return self.sendMsg(content, retry-1)
                else:
                    Util.echo(u"[Error] getToken() failed. token = %s" % self.access_token)
                    return False
            else:
                return True
        except Exception as exp:
            Util.echo(u"[Error] sendMsg(), %s" % repr(exp))
            traceback.print_exc()
            return False
        return True

def test():
    w = QYWeixinMsg()
    w.sendMsg(u'测试1')

if __name__ == '__main__':
    test()
