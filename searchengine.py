# -*- coding:UTF-8 -*-
import urllib


class crawler:
    # 初始化, 并传入 数据库名称
    def __init__(self,dbname):
        pass
    def __del__(self):
        pass
    def dbcommit(self):
        pass
    # 获取 条目的id,如果条目不在,就加入数据库中
    def getentryid(self,table,field,value,createnew=True):
        return None
    # 为每个网页建立索引
    def addtoindex(self,url,soup):
        print 'Indexing %s' % url
    # 从网页中提取网页
    def gettextonly(self,soup):
        return None
    # 对非空白字符进行分词处理
    def separatewords(self,text):
        return None
    # 已建立索引,则返回 True
    def isindexed(self,url):
        return False
    # 添加关联两个网页的链接
    def addlinkref(self,urlFrom,urlTo,linkText):
        pass
    # 从某网页进行广度搜索,直至某一给定深度
    def crwal(self,pages,depth=2):
        pass
    # 创建数据库
    def createindextable(self):
        pass
    
    
# 下载文件,url 地址, fname 保存的文件名   
def download_file(url,fname):
    urllib.urlretrieve(url,fname)

def open(url):
    import urllib2
    c = urllib2.urlopen(url)
    contents = c.read()
    return contents.decode('gbk','ignore')


def test_twill(url):
    from twill import get_browser
    b = get_browser()    
    b.go(url)
    b.showforms()

    pass

def main():
    url = "http://202.114.74.198"
    contents = open(url)
    print contents
    #test_twill(url)
    
    
if __name__ == "__main__":
    main()