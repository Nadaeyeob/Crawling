import sys
import io
from tinydb import TinyDB, Query, where
from tinydb.storages import MemoryStorage
import simplejson as json

# 메모리 DB 생성
db = TinyDB('C:/Users/sw993/Crawling/databases/database1.db')

# db.insert({'name' : 'kim', 'email' : 'test@gmail.com'}) # dict 형식 -> json형식으로 삽입
# db.insert_multiple([{'name' : 'kim', 'email' : 'test@gmail.com'},{'name' : 'lee', 'email' : 'aaa@gmail.com'}]) # jsonAraay(dict) [{},{},{}]

SQL = Query()

el = db.get(SQL.name == 'kim')

print(el)
print(el.doc_id)

# Data 수정
# db.update({'email':'test1@google.com'}, doc_ids=[1])

# Data 수정 및 추가
db.upsert({'email' : 'test1@naver.com', 'login' : True},SQL.name == 'park')
# upsert = Update + Insert, 있는 것은 수정하고 없는 것은 추가함

# db.remove(doc_ids=[1])
db.remove(SQL.name=='park')

print(db.all())
