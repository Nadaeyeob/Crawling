import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# ORM Object-relational mapping
# 객체 관계형 Mapper Database Table -> 파이썬 클래스(변수) 등 변경시 적용될 수 있게끔 함

import pandas_datareader.data as web
import pandas as pd
import datetime
import sqlite3

# pandas, pandas_datareader 설치
try:
    with sqlite3.connect('C:/Users/sw993/Crawling/Section5/databases/sqlite2.db') as conn:
        pass
        # 조회 시작 & 마감 날짜
        start = datetime.datetime(2020,1,1)
        end = datetime.datetime(2020,12,1)

        # google 정보 호출
        gs = web.DataReader('090430','naver',start,end) # 주가 읽기
        # print(gs)
        # print(gs.index)
        # print(gs['Open'])
        # print(gs.iloc[124])

        # index to column
        gs['Date'] = gs.index
        gs.index = range(1,len(gs.index)+1)
        # print(gs)

        # Database 에 Table 생성 -> Data를 Insert -> commit()

        # pandas to Database(to_sql)
        # gs.to_sql("AMOLE",conn, if_exists='fail',index=True, index_label='id') # fail,replace, append
        gs.to_sql("AMOLE",conn, if_exists='replace',index=True, index_label='id') # fail,replace, append

        # fail : table이 있을 경우 실행하지 않음
        # replace : 기존 Data 삭제
        # appned : 기존 Database에 새로운 Data 추가

        # commit 반영
        # conn.commit()

        # pandas read DataBase(read_sql)
        df = pd.read_sql(('SELECT * FROM AMOLE'), conn,index_col = 'id') # index_col = 'id'
        print(df)

        # pandas read DataBase(read_sql) 조건조회
        df = pd.read_sql(("SELECT * FROM AMOLE WHERE id = ? or id = ?"),conn,params=(120,150),index_col='id')
        print(df)
finally:
    print('Dataframe SQL Work Complete')
