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
for x in write_filter:
    if x in words:
        words = words.replace(x,'*'*len(x))
print(words)