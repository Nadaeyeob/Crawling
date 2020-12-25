import sys
import io
from tinydb import TinyDB, Query, where
from tinydb.storages import MemoryStorage
import simplejson as json

# 메모리 DB 생성
db = TinyDB('C:/Users/sw993/Crawling/databases/database.db')

users = db.table('users')
todos = db.table('todos')

Users = Query()
Todos = Query()

# 여러가지 조회 방법
print(users.search(Users.id == 7))
print(users.search(Users['id'] == 7))
print(users.search(where('id') == 7))
print(users.search(Query()['id'] == 7))
print(users.search(where('address')['zipcode'] == '58804-1099'))

# 고급 Query
print(users.search(Users.email.exists())) # email key 값을 가지고 있는 항목 반환
print(users.search(Users.aaa.exists())) # aaa라는 Key 가 없음으로 null list 반환

# NOT
print('NOT',users.search(~(Users.username == 'Bret')))  # Bret 을 제외하고 Print 함

# OR
print('OR',users.search((Users.username == 'Bret') | (Users.username == 'Antonette')))

# AND
print('AND',users.search((Users.username == 'Bret') & (Users.email == 'Sincere@april.biz')))

# 기타함수
print('len',len(users))
print('len',len(todos))
print('contains', users.contains(Users.username == 'Bret'))
print('count', users.count(Users.username == 'Bret'))
