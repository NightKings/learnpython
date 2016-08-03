#coding:utf-8
import os.path,os,re
L = [x for x in os.listdir('dairy')]
for x in L:
    write_word = {}
    s = 'dairy\\' + x
    with open(s,'r') as f:
        lines = f.readlines()
        for word in lines:
            words = re.findall('\w{5,20}',word)
            for x in words:
                if x not in write_word:
                    write_word[x] = 1
                else:
                    write_word[x] += 1
        List  = sorted(write_word.items(),key = lambda t : t[1],reverse = True)
        v = 0
        k=''
        for key,value in List:
            if value>v:
                k = key
                v = value
        print(k,v)