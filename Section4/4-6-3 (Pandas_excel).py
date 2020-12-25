import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import pandas as pd
import numpy as np

# Random DataFrame 생성
df = pd.DataFrame(np.random.randint(0,100,size=(100,4)), columns=list('ABCD'))
# df = pd.DataFrame(np.random.randint(0,100,size=(100,4)), columns=['A','B','C','D'] 와 같음
df = pd.DataFrame(np.random.randn(100,4), columns=['A','B','C','D'])
print(df)

df.to_excel(r'c:/crawling/section4/np_1.xlsx',index=False)
