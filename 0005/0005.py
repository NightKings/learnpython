#coding:utf-8
from PIL import Image,ImageOps
import os,os.path
L = [ x for x in os.listdir('iPhone5')]
for x in L:
    s = 'iPhone5\\' + x
    im = Image.open(s)
    im = ImageOps.fit(im,(1136,640))
    im.save('.\iPhone5\\IP'+ x)