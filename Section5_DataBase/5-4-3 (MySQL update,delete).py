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

try:
    with conn.cursor() as c:
        # data 수정1
        c.execute("UPDATE users SET username = %s WHERE id=%s",('niceman',1))
        c.execute("UPDATE users SET username = '%s' WHERE id='%d'"%('goodboy',2)) # python fomatting

        # 중간 Data 확인1
        c.execute("SELECT * FROM users ORDER BY id DESC")
        for row in c.fetchall():
            print('check1>',row)

        # Data 삭제1
        c.execute("DELETE FROM users WHERE id = %s",(1,))
        # Data 삭제2
        c.execute("DELETE FROM users WHERE id = '%s'" %(2,))

    conn.commit()

finally:
    conn.close()
