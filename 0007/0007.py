#cod:utf-8
import os,os.path,re
L = os.listdir('mycode')
code,note,space = 0,0,0
for x in L:
    path = 'mycode\\' + x
    with open(path,'r') as f:
        lines = f.readlines()
    for x in lines:
        if re.match(r'^\s+\w',x):
            code+= 1
        elif re.match(r'\#\w+',x):
            note += 1
        else:
            space += 1
print('code:%d'%code)
print('space:%d'%space)
print('note:%d'%note)