import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import pandas as pd

# df = pd.read_csv('C:/Crawling/Section4/csv_s1.csv')
# df = pd.read_csv('C:/Crawling/Section4/csv_s1.csv',skiprows=[0,1])
# df = pd.read_csv('C:/Crawling/Section4/csv_s1.csv', header=1)
# df = pd.read_csv('C:/Crawling/Section4/csv_s1.csv', skiprows=[0], header=None, names=['Month',2013,2014,2015])
# -> Index custom 설정
# df = pd.read_csv('C:/Crawling/Section4/csv_s1.csv', skiprows=[0], header=None, names=['Month',2013,2014,2015], index_col=[0], na_values=['JAN'])

df = pd.read_csv('C:/Crawling/Section4/csv_s1.csv', skiprows=[0], header=None, names=['Month',2013,2014,2015])
print(df.index) # RangeIndex(start=0, stop=12, step=1)
print(list(df.index))
print(df.index.values)
print(df.index.values.tolist())

# print(df.rename(index={0:'aa',1:'bb'})) cols name을 dict형태로 바꿔줘야함
print(df.rename(index = lambda x:x+1))

# 읽기
# df = pd.read_csv(r'C:/Crawling/Section4/csv_s2.csv',sep=';')
df1 = pd.read_csv(r'C:/Crawling/Section4/csv_s2.csv',sep=';',skiprows=[0],header=None,names=['Name','Test1','Test2','Test3','Final','Grade'])

print(df1)
df1['Grade1'] = df1['Grade'].str.replace('C','A++')
df1['avg'] = df1[['Test1','Test2','Test3','Final']].mean(axis=1)
df1['sum'] = df1[['Test1','Test2','Test3','Final']].sum(axis=1)
print(df1)
