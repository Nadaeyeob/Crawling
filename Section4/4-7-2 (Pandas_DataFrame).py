import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import pandas as pd
from pandas import Series,DataFrame
import numpy as np

r_data = {'city' : ['서울','대구','부산','대전'],'total1' : [55,49,52,50], 'total2' : [56,24,74,98]}
print(type(r_data))
print(type(DataFrame(r_data)))
i_data = ['one','two','three','four']
print(r_data)
print(i_data)
# 출력
print('------')
df = DataFrame(r_data, index=i_data)
print(type(df))
print(df)
print(df.index)
print(df.values)
print(df['city']) # columns
print(df.iloc[0,:]) # rows
df = df.reset_index()
print(df.isin(['one','two']))

for e in df.values:
    for i,z in enumerate(e):
        print(i,z)
