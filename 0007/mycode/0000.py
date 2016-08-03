#coding: utf-8
from PIL import Image,ImageDraw,ImageFont

def addnum(pic):
    im = Image.open(pic)
    x,y = im.size
    font = ImageFont.truetype('PICOSUB_.ttf',90)
    draw = ImageDraw.Draw(im)
    draw.text((x-110,100),'4',font=font,fill=(255,0,0))
    im.save('0000.jpg','jpeg')
if __name__ == '__main__':
    addnum('6.jpg')