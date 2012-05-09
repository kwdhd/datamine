# -*- coding:UTF-8 -*-
import config
import urllib2
import urllib
import download_pic

def login():
    isLogin = False
    while not isLogin:
        # 读取验证码
        download_pic.download_pic(config.url,1)
        # 识别
        download_pic.pretreatment('./yzm/0000.png')
        yzms = download_pic.recognize('./yzm/0000.tif').strip()
        print yzms
        #yzms.trim()
        # 反复提交
        values = "who=guest&id=&pwd=&yzm="+yzms+"&submit=%C8%B7+%B6%A8"#(确定的gb码)
        #values = {'who':'guest','id':'','pwd':'','yzm':yzms,'submit':"确定"}
        print values
        #postdata = urllib.urlencode(values) 
        #print postdata
        req = urllib2.Request(config.loginform, values) # 服务器请求 
        print 'request:'
        print req
        response = urllib2.urlopen(req) 
        print 'response:'
        print response
        the_page = response.read()
        return the_page.decode('gbk','ignore')
        # 返回结果 True or False
    pass

def get(url,data):
    pass

def post(url,param):
    pass

def main():
    print login()
    
if "__main__" == __name__:
    main()