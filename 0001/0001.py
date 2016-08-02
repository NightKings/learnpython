#coding:utf-8
import random
def random_generate():
    s = ''
    for x in range(1,20):
        s += chr(random.randint(65, 90))
    s += '\n'
    return s
def savetxt():
    with open('result.txt','a') as f:
        f.write(random_generate())
if __name__ == '__main__':
    for x in range(0,200):
        savetxt()