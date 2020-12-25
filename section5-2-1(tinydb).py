import sys
import io
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
import simplejson as json

# 메모리 DB 생성
db = TinyDB('C:/Users/sw993/Crawling/databases/database.db')

# db = TinyDB(storage=MemoryStorage, default_table='users')

users = db.table("users")
todos = db.table('todos')

# Table Data 삽입
# users.insert({'name' : 'kim', 'email' : 'test@google.com'})
# todos.insert({'name' : 'homework', 'complete' : False})

# Table Data 전체 삽입1
with open('C:/Users/sw993/Crawling/data/users.json','r') as infile:
    r = json.loads(infile.read())
    for u in r:
        # print(u)
        users.insert(u)

# Table Data 전체 삽입2
with open('C:/Users/sw993/Crawling/data/todos.json','r') as infile:
    r = json.loads(infile.read())
    for t in r:
        # print(t)
        todos.insert(t)
# 전체 Data 출력
print(users.all())
print(todos.all())

# table 목록 조회
print(db.tables())

# 전체 Data 삭제
# users.truncate() # db.truncate() -> Table도 날아감
# todos.truncate()

db.close() # 시작을 with로 하면 상관 없음
