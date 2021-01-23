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

# try:
#     with conn.cursor() as c: # conn.cursor(pymysql.cusors.DictCursor)
#         c.execute("SELECT * FROM users")
#         # 1개 row
#         print(c.fetchone())
#         # 선택지정
#         print(c.fetchmany(3))
#         # 전체 Row
#         print(c.fetchall())
# finally:
#     conn.close

# try:
#     with conn.cursor(pymysql.cursors.DictCursor) as c: #-> List로 반환
#         c.execute("SELECT * FROM users")
#         # 1개 row
#         print(c.fetchone())
#         # 선택지정
#         print(c.fetchmany(3))
#         # 전체 Row
#         print(c.fetchall())
# finally:
#     conn.close

try:
    with conn.cursor() as c: # conn.cursor(pymysql.cusors.DictCursor)
        c.execute("SELECT * FROM users")

        # 순회1
        rows = c.fetchall()
        c.execute("SELECT * FROM users ORDER BY id ASC")
        for row in rows:
            print('usage1>',row)

        # 순회2
        c.execute("SELECT * FROM users ORDER BY id DESC")
        for row in c.fetchall():
            print('usage2>',row)

        # 조건 조회1
        param1 = (1,)
        c.execute("SELECT * FROM users WHERE id=%s", param1)
        print(c.fetchall())

        # 조건 조회2
        param2 = 2
        c.execute("SELECT * FROM users WHERE id=%d" %param2) # python formatting
        print(c.fetchall())

        # 조건 조회3
        param3 = (4,5)
        c.execute("SELECT * FROM users WHERE id IN(%s,%s)",param3)

        # 조건 조회4
        # c.execute("SELECT * FROM users WHERE id IN('%s','%s')" %param3)
        c.execute("SELECT * FROM users WHERE id IN('%d','%d')" % (4,5))
        print(c.fetchall())

finally:
    conn.close
