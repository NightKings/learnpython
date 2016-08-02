#coding:utf-8
import redis
def get_lines(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    for x in range(0,200):
        lines[x] = lines[x].strip()
    return lines
def writein():
    lines = get_lines('result.txt')
    r = redis.StrictRedis(host='192.168.0.212',port=6379,db = 0)
    for n in range(0,200):
        key = str(n+1)
        value = str(lines[n])
        r.set(key,value)
    r.save()
if __name__ == '__main__':
    writein()