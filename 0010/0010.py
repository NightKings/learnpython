#coding: utf-8
from PIL import Image,ImageFilter,ImageDraw,ImageFont
import random
def radChar():
    return chr(random.randint(65,90))
def radColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
def radColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
width = 60*4
height = 60
im = Image.new('RGB',(width,height),(255,255,255))
font = ImageFont.truetype('PICOSUB_.ttf',36)
draw = ImageDraw.Draw(im)
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=radColor())
for t in range(4):
    draw.text((60*t+10,10),radChar(),font=font,fill=radColor2())
im = im.filter(ImageFilter.BLUR)
im.save('code.jpg','jpeg')