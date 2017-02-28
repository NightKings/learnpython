#coding:utf-8
import pymysql
def read_line():
    with open('result.txt','r') as f:
        lines = f.readlines()
    for n in range(0, 200):
        lines[n] = lines[n].strip()
    return lines
def connect():
    try:
        conn = pymysql.connect(host = '192.168.0.212',user = 'root',passwd='XXXX',port = 3306,use_unicode=True)
        cur = conn.cursor()
    except:
        raise EOFError('Error')
    return (conn,cur)
def Iinsert(conn,cur):
    lines = read_line()
    try:
        cur.execute('create database gift;')
    except:
        pass
    cur.execute('use gift');
    try:
        cur.execute('create table gifts(id INT (20),gift VARCHAR (20));')
    except:
        pass
    for x in range(0,200):
        cur.execute('insert into gifts(id,gift) VALUES (%d,\'%s\')'%(x+1,lines[x]))
    conn.commit()
    conn.close()
if __name__ == '__main__':
    conn,cur = connect()
    Iinsert(conn, cur)
