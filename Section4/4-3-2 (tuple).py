# List 자료형(순서 O, 중복 O, 수정 x, 삭제 x) indexing, slicing 모두 동일하나 수정 삭제 불변

# 속도 tuple > list

a = ()
b = (0,) # 원소 한개를 넣을땐 ,를 찍어줘야함
c = (1,1,1,2)
d = (0,1,'car','apple','apart') # 서로 다른 특성도 담을 수 있음
e = (1,2,('car','apple','apart')) # List 안에 List 가능

# indexing
print('------')
print('d - ',type(d),d)
print('d - ', d[0])
print('d - ', d[0]+d[1])
print('e - ', e[2][2]) # print('e - ',e[-1][2])

# slicing
print('------')
print('d - ',d[0:3])
print('d - ',d[2:])

# 연산
print('------')
print('c + d',c + d)
print('c * 3',c * 3)
print('hi + c[0]', 'hi' + str(c[0]))

# tuple 함수 -> idnex와 count만 제공
a = (5,2,3,1,4)
