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

# 날짜 생성
now = datetime.datetime.now()
print(now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

# version 확인
print(sqlite3.version) # sqlite3 자체 version
print(sqlite3.sqlite_version) # core version

# Cursor 연결
c = conn.cursor()
print(type(c))

# Table 생성(SQLite3 Datatype : Text,Numeric,Integer,real,BLOB)
# BLOB 파일형 저장할 때 사용
c. execute('CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, username TEXT, email text, phone text, website text, regdate text)')
#AUTOINCREMENT 사용 시 자동으로 ID 생성 (순서별로)

# Data 삽입
# c.execute("INSERT INTO users VALUES(1,'kim','kim@naver.com','010-0000-0000','kime.co.kr',?)",(nowDatetime,))
# tuple일 경우 List 와 다르게 , 필요 - (nowDatetime 항목)

userList = (
    (2,'kim','kim@naver.com','010-0000-0000','kime.co.kr',nowDatetime),
    (3,'kim','kim@naver.com','010-0000-0000','kime.co.kr',nowDatetime),
    (4,'kim','kim@naver.com','010-0000-0000','kime.co.kr',nowDatetime)
)
# c.executemany('insert into users(id, username, email, phone, website, regdate) values(?,?,?,?,?,?)',userList)

# jsondata 삽입
with open('C:/Users/sw993/Crawling/Section5/data/users.json','r') as infile:
    r = json.load(infile)
    userData = []
# executemany 사용하려면 Tuple로 만들어야함, 하지만 Tuple은 append가 없음(수정이 안됌)
# -> List를 만든 후 Tuple로 변환
    for user in r:
        t = (user['id'],user['name'],user['email'],user['phone'],user['website'],nowDatetime)
        # print(t) -> Data를 Tuple로 선언
        userData.append(t)
    # print(userData) -> List 형태
    # print(tuple(userData)) -> Tuple로 변환

    c.executemany('insert into users(id, username, email, phone, website, regdate) values(?,?,?,?,?,?)',userData)
# python 에서 list를 넣어도 tuple로 형변환하여 올려주기 때문에 별도로 Tuple로 형변화 안해도 사용 가능

# print('users db delete', conn.execute('delete from users').rowcount,'rows')
# truncate 를 사용할 경우 Data 구조는 남기고 Data만 삭제
conn.commit()

conn.close() # with로 시작해서 크게 문제는 없음
