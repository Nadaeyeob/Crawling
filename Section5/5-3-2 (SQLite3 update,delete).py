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

# Data update
c.execute("UPDATE users SET username= ? WHERE id=?", ('niceman',1))
c.execute("UPDATE users SET username= :name WHERE id=:id", {"name":'goodboy',"id":2})
c.execute("UPDATE users SET username='%s' WHERE id='%s'"%('cuteboy',3))

# Data delete
c.execute("DELETE FROM users WHERE id = ?",(1,))

# 중간 Data 확인
for user in c.execute("SELECT * FROM users"):
    print(user)

conn.commit()
conn.close()
