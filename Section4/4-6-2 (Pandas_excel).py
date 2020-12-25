import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import pandas as pd


df1 = pd.read_excel('c:/crawling/section4/excel_s1.xlsx',engine='openpyxl',sheet_name=0)
print(df1)
df1['State'] = df1['State'].str.replace('','|')
print(df1['State'])
print('------')
df1['avg'] = df1[['2003','2004','2005']].mean(axis=1).round(2)
print(df1)
print('------')
df1.info()
print('------')
print(df1[['2003','2004','2005']].max(axis=0))
print(df1.describe())

df1.to_excel('c:/crawling/section4/excel_s1_1.xlsx',engine='openpyxl')
