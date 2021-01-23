import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import sqlite3
import simplejson as json
import datetime

# DB 생성
# conn = sqlite3.connect('C:/Users/sw993/Crawling/Section5/databases/sqlite1.db',isolation_level=None)
# isolation_level = None -> AutoCommit, 사용하지 않을 경우 conn.commit() 등을 명시적으로 사용해야함

# 1회성 Memory 할당 (Memory DB)
# conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('C:/Users/sw993/Crawling/Section5/databases/sqlite1.db')
c = conn.cursor()

# Data 조회(전체)
c.execute('select * from users')

#1개 row 선택
# print(c.fetchone())

# 지정 row 선택
# print(c.fetchmany(size=4)) #1은 위에서 cursor 위치가 넘어감

# 전체 row 선택
# print(c.fetchall()) # 위 구문에서 5까지 넘어감
# print(c.fetchone()) # None

# 순회1
rows = c.fetchall()
for row in rows:
    print('usage1 : ',row )

# 순회2
for row in c.fetchall():
    print('usage2 : ',row)

# 순회3
for row in c.execute('select * from users'):
    print('usage3 : ',row)

# 조건 조회1
param1 = (1,)
c.execute('select * from users where id=?',param1)
print(c.fetchall())

# 조건 조회2
param2 = 2
c.execute("select * from users where id='%s'"%param2) # python에서 쓰는 %s,%d,%f,%o 와는 다름 - python format
print(c.fetchall())

# 조건 조회3
c.execute('select * from users where id=:id',{'id':3})
print(c.fetchall())

# 조건 조회4
param4 = (1,4)
c.execute("select * from users where id in (?,?)",param4)
print(c.fetchall())

# 조건 조회5
c.execute("select * from users where id=:id1 or id=:id2",{"id1":2,"id2":3})
print(c.fetchall())

# dump
with conn:
     # Dump 출력
     with open('C:/Users/sw993/Crawling/Section5/data/test.dump','w') as f:
         for line in conn.iterdump():
             f.write('%s\n' %line)
             print('Dump write complete')
