import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# MySQL : Oracle
# MariaDB : GPL V2

import pymysql
import simplejson as json
import datetime

# MySQL connection
conn = pymysql.connect(host='localhost',user='python', password='1111!',
                        db = 'python_app1',charset='utf8')

# pyMySQL version 확인
print('pymysql.version',pymysql.__version__)

# Database 선택
conn.select_db('python_app1')

# Cursor
c = conn.cursor()
print(type(c))

# Database 생성
# c.execute('create database python_app2') # 권한이 있을 경우 Database 생성 가능, DML, DDL, DCL

# Cursor 반환
# c.close()

# 접속 해제
# conn.close()

# Transaction 시작 선언
conn.begin()

# commit
conn.commit()

# Rollback
conn.rollback()

# 날짜 생성
now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H-%M-%S')
print(nowDatetime)

# c.execute("CREATE TABLE IF NOT EXISTS users(id bigint(20) NOT NULL AUTO_INCREMENT DEFAULT 'TEST)")
c.execute("CREATE TABLE IF NOT EXISTS users(id bigint(20) NOT NULL, \
            username varchar(20),\
            email varchar(30),\
            phone varchar(30),\
            website varchar(30),\
            regdate varchar(20) NOT NULL, PRIMARY key(id))"\
        )

try:
    with conn.cursor() as c:
        #json to MySQL
        with open('C:/Users/sw993/Crawling/Section5/data/users.json','r') as infile:
            r = json.load(infile)
            userData = []
            for user in r:
                t = (user['id'],user['username'],user['email'],user['phone'],user['website'],nowDatetime)
                userData.append(t)
                # c.execute("INSERT INTO users(id,username,email,phone,website,regdate\
                #           VALUES (%s,%s,%s,%s,%s,%s)", t)
            c.executemany("INSERT INTO users(id,username,email,phone,website,regdate) \
                            VALUES (%s,%s,%s,%s,%s,%s)",tuple(userData))
        conn.commit()
finally:
    conn.close()
