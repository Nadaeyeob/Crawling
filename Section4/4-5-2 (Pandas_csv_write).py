import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import pandas as pd


# 읽기
# df = pd.read_csv(r'C:/Crawling/Section4/csv_s2.csv',sep=';')
df1 = pd.read_csv(r'C:/Crawling/Section4/csv_s2.csv',sep=';',skiprows=[0],header=None,names=['Name','Test1','Test2','Test3','Final','Grade'])

df1['Grade1'] = df1['Grade'].str.replace('C','A++')
df1['avg'] = df1[['Test1','Test2','Test3','Final']].mean(axis=1)
df1['sum'] = df1[['Test1','Test2','Test3','Final']].sum(axis=1)
print(df1)

df1.to_csv(r'C:/crawling/Section4/csv_s2_write.csv',index=False)
