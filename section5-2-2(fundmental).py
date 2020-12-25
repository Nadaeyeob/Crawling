import sys
import io
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
import simplejson as json

# 메모리 DB 생성
db = TinyDB('C:/Users/sw993/Crawling/databases/database.db')

# db = TinyDB(storage=MemoryStorage, default_table='users')

users = db.table('users')
todos = db.table('todos')

for item in users:
    pass
    # print(item['name'], ' : ' , item['phone'])

for list in todos:
    pass
    # print(list['title'], ' : ', list['completed'])

for item in users:
    pass
    # print('[',item['username'],']')
    for list in todos:
        if list['userId'] == item['id']:
            # print(list['title'])
            pass

# Query 객체 사용 조회
# SQL = Query()
Users = Query()
Todos = Query()

# table 내 data 수정
users.update({'username' : 'kim'}, Users.id == 3)

user_3 = users.search(Users.id == 3) #<,>,<=,>=
print(user_3)

# table 내 data 삭제
users.remove(Users.id == 3)
print(users.search(Users.id == 3))
