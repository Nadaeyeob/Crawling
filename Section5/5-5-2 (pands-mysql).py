import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# ORM Object-relational mapping
# 객체 관계형 Mapper Database Table -> 파이썬 클래스(변수) 등 변경시 적용될 수 있게끔 함

import pandas_datareader.data as web
import pandas as pd
import datetime
import pymysql

# MySQLdb 생성
pymysql.install_as_MySQLdb()
import MySQLdb
from sqlalchemy import create_engine

# pymysql, sqlalchemy 설치
try:
    # 엔진 생성
    engine = create_engine("mysql+mysqldb://python:"+'1111!'+"@localhost/python_app1",encoding='utf8')
    with engine.connect() as conn:
        pass
        # 조회 시작 & 마감 날짜
        start = datetime.datetime(2020,1,1)
        end = datetime.datetime(2020,12,1)

        # google 정보 호출
        gs = web.DataReader('035720','naver',start,end) # 주가 읽기
        gs['Date'] = gs.index
        gs.index = range(1,len(gs.index)+1)

        gs.to_sql("kakao",conn, if_exists='replace',index=True, index_label='id') # fail,replace, append

        # fail : table이 있을 경우 실행하지 않음
        # replace : 기존 Data 삭제
        # appned : 기존 Database에 새로운 Data 추가

        # commit 은 autocommit임
        # conn.commit()

        # pandas read DataBase(read_sql)
        print('------')
        df = pd.read_sql(("select * from kakao"), conn,index_col = 'id') # index_col = 'id'
        print(df)
        print('------')
        # pandas read DataBase(read_sql) 조건조회
        df = pd.read_sql("select * from kakao where id = %s or id = %s",conn,params=(120,150),index_col='id')
        print(df)
finally:
    print('Dataframe SQL Work Complete')
    # conn은 with문에서 닫히지만, engine도 닫는게 좋음
    engine.dispose()
