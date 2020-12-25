import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

import pickle # 객체,Text를 직렬화, 역직렬화

# 파일 이름과 데이터
bfilename = 'c:/crawling/Section4/test.bin'
tfilename = 'c:/crawling/Section4/test.txt'

data1 = 77
data2 = 'hello, world!'
data3 = ['car','apple','house']

# binary 쓰기
with open(bfilename, 'wb') as f:
    pickle.dump(data1,f) # dump 객체, dumps Text(문자열) 직렬화
    pickle.dump(data2,f)
    pickle.dump(data3,f)

# Text 쓰기
with open(tfilename, 'wt') as f:
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    # f.writelines(data3) # carapplehouse 를 붙여버림
    f.writelines('\n'.join(data3))

# binary 읽기, text를 읽어오면 그냥 String
with open(bfilename, 'rb') as f:
    b = pickle.load(f) # loads 는 문자열 역직렬화
    print(type(b), ' binary read1 | ',b)
    b = pickle.load(f)
    print(type(b), ' binary read2 | ',b)
    b = pickle.load(f)
    print(type(b), ' binary read3 | ',b)

# text 읽기
with open(tfilename, 'rt') as f:
    for i, line in enumerate(f,1):
        print(type(line),'Text Read' + str(i) + '| ',line, end='')
