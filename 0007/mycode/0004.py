#coding:utf-8
import re
counts = 0
with open('1.txt','r') as f:
    lines=f.readlines()
for line in lines:
    word = re.findall(r"\w+",line)
    counts += len(word)
print(counts)