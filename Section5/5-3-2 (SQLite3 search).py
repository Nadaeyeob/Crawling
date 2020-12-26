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
