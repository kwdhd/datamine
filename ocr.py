#encoding=utf-8
import Image,ImageEnhance,ImageFilter
import sys
from pytesser import *


image_name = "genimg"

def main():

    #Image.open(image_name+".jpg").convert('RGB').save(image_name+".tif")
    im = Image.open("test.tif")
    text = image_to_string(im)
    print text
    raw_input()
    pass

if __name__ == "__main__":
    main()