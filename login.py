# -*- coding:UTF-8 -*-
import config
import cookielib, urllib2
import urllib
from urllib import urlencode
import download_pic

def login():
    # 打开首页,获取 cookie
    # 重试直到 成功 or retry_num
    # 读取验证码
    # 提交表单
    # 验证返回结果
    # 写 cookie
    pass

def fetch_pub():
    # 读取 cookie
    # 提交查询
    # 与数据库信息进行比较
    pass
    
def test_login():  
    #登陆页面，可以通过抓包工具分析获得，如fiddler，wireshark  
    login_page = config.loginform
    url = 'http://202.114.74.198/stu/choose_pubLesson_list.jsp?actionType=query'
    
#    try:  
    while True:
        enable_proxy = True
        proxy_handler = urllib2.ProxyHandler({"http" : '192.168.1.1:8888'})
        null_proxy_handler = urllib2.ProxyHandler({})
         
        if enable_proxy:
            opener = urllib2.build_opener(proxy_handler)
        else:
            opener = urllib2.build_opener(null_proxy_handler)
         

        #获得一个cookieJar实例  
        cj = cookielib.MozillaCookieJar("cookie")  
        #cookieJar作为参数，获得一个opener的实例  
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)) 
        urllib2.install_opener(opener) 
        #伪装成一个正常的浏览器，避免有些web服务器拒绝访问。  
        opener.addheaders = [('User-agent','Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0'),("Accept"," text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),("Accept-Language","en-us,en;q=0.5"),("Accept-Encoding","gzip, deflate"),("Connection","keep-alive"),("Referer","http://xk.whu.edu.cn")] 
        # 打开登录页
        content = urllib2.urlopen('http://202.114.74.198/').read().decode('gbk','ignore') 

        print 'content',content
        #生成Post数据，含有登陆用户名密码。  
        # 读取验证码
        #download_pic.download_pic(config.url,1)
        pic = urllib2.urlopen('http://202.114.74.198/GenImg').read()
        yzm = open('./yzm/0000.png','wb')
        yzm.write(pic)
        yzm.close()
        # 识别
        download_pic.pretreatment('./yzm/0000.png')
        yzms = download_pic.recognize('./yzm/0000.tif').strip()
        print yzms
        print 'cookie',cj
        cj.save(ignore_discard=True, ignore_expires=True)
        #yzms.trim()
        # 反复提交
        values = "who=guest&id=&pwd=&yzm="+yzms+"&submit=%C8%B7+%B6%A8"#(确定的gb码)
        # requset
        request = urllib2.Request(url = login_page,data = values)
        #request = opener.open(login_page,values) 
        print 'request',request
        result = urllib2.urlopen(request).read()
        cj.save(ignore_discard=True, ignore_expires=True)
        print 'result',result.decode('gbk','ignore')
        #以post的方法访问登陆页面，访问之后cookieJar会自定保存cookie  
        #opener.open(login_page,values)  
        #以带cookie的方式访问页面  
        op=opener.open(url)  
        #读取页面源码  
        data= op.read()  

        return data.decode('gbk','ignore')  
#    except Exception,e:  
#        print 'error',str(e)  

def login1():
    isLogin = False
    while not isLogin:
        # 打开登录页
        cj = cookielib.LWPCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0)"),("Accept", "text/html, image/jpeg, image/png, text/*, image/*, */*")]
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
        the_page = response.read()
        print 'response:'
        print response.getcode()
        print response.info()
        return the_page.decode('gbk','ignore')
        # 返回结果 True or False
    pass

def get(url,data):
    pass

def post(url,param):
    pass

def main():
    #print login()
    print test_login()
    
if "__main__" == __name__:
    main()