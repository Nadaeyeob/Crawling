import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import pandas as pd


df1 = pd.read_excel('c:/crawling/section4/excel_s1.xlsx',engine='openpyxl',sheet_name=0)
# df1 = pd.read_excel('c:/crawling/section4/excel_s1.xlsx',engine='openpyxl',sheet_name=0, skip_footer=10)
# -> 아래로부터 10개 생략
# df1 = pd.read_excel('c:/crawling/section4/excel_s1.xlsx',engine='openpyxl',sheet_name=0, header=0)

print(df1.head(3))
print(df1.tail(3))
print(list(df1.columns.values))
col = [4,5,6]
df1.drop(df1.columns[col],axis=1, inplace=True)
print('------')
df2 = pd.read_excel('c:/crawling/section4/excel_s1.xlsx',engine='openpyxl',sheet_name=0,header=None,names=['state',2003,2004,2005])
print(df2)
# col = [4,5,6]
# df2.drop(df1.columns[col],axis=1, inplace=True)

df1.drop([52,53],inplace=True)
print(df1)
