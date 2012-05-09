# -*- coding:UTF-8 -*-
import urllib, random  
import Image,ImageEnhance,ImageFilter
import sys,os
from pytesser import *


def download_pic(url,num):
    for i in range(num):   
        print "download", i  
        file("./yzm/%04d.png" % i, "wb").write(urllib.urlopen(url).read())

# 取字模      
def take_matrix(image_name):
    pass

# 图片预处理
def pretreatment(image_name):
    #去处 干扰点
    im = Image.open(image_name)
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    #保存
    fname = image_name.split('.')
    print image_name
    print fname
    im.convert('RGB').save("."+fname[1]+'.tif')
#
def convert_to_tif(image_name):
    im = Image.open(image_name)
    fname = image_name.split('.')
    im.convert('RGB').save("."+fname[1]+'.tif') 
# 对所有图片进行预处理
def pretreat_all(fpath,type):
    import glob
    filelist = glob.glob(fpath+"*."+type) 
    #print filelist
    for pic in filelist:
        pretreatment(pic)
       
# 识别
def recognize(fname):
    im = Image.open(fname)
    text = image_to_string(im)
    return text

def recognize_all(fpath):
    import glob
    type = 'tif'
    filelist = glob.glob(fpath+"*."+type) 
    #print filelist
    results = []
    for pic in filelist:
        results.append(recognize(pic))
    return results

def main():
    url = 'http://202.114.74.198/GenImg'
    num = 100
    save_path = "\\yzm\\converted\\"
    yzm_path = ".\\yzm\\"
    pic_type = "png"
    
    #download_pic(url,num)
    pretreat_all(yzm_path,pic_type)
    res = recognize_all(yzm_path)
    for r in res:
        print r
    pass

if __name__ == "__main__":
    main() 