#coding:utf-8
import os,re
x=0
write_filter = set()
with open('filtered_words.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        lines[x] = lines[x].strip()
        x+=1
    for x in lines:
        write_filter |= {x}
words = input('Enter -')
flag = 0
for x in write_filter:
    if x in words:
        flag = 1
if flag == 0:
    print('Human Rights')
else:
    print('freedom')