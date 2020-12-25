a = 'hello'
print(type(a))
print(a[0]) # List 형태는 아니지만, List로 출력함
print(a[0:3])

for i in a:
    print(i)
    print(type(i))

print('------')

# List 자료형(순서 O, 중복 O, 수정 O, 삭제 O)
a = []
b = list()
c = [1,1,1,2]
d = [0,1,'car','apple','apart'] # 서로 다른 특성도 담을 수 있음
e = [1,2,['car','apple','apart']] # List 안에 List 가능

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

# List 수정,삭제
print('------')
c[0] = 4
print('c - ',c)
c[1:2] = ['a','b','c']
print('c - ',c) # List 안에 List가 아닌 원소로 넣음
c[1] = ['a','b','c']
print('c - ',c) # index 지정해서 넣을 시 List로 넣음
c[1:3] = []
print('c - ',c) # 1부터 3까지 사라짐
del c[3]
print('c - ',c)

# List 함수
a = [5,2,3,1,4]
print('------')
print('a - ',a)
a.append(6) # 끝에 삽입
print('a - ',a)
a.sort()
print('a - ',a)
a.reverse()
print('a - ',a)
# a.index(4) = a[4]
print('a - ',a.count(1)) # '1' 이 몇 개인지 계산
a.remove(2) # 원소값이 삭제됌
print('a - ',a)
print('a - ',a.pop()) # 맨 마지막 숫자가 빠짐
print('a - ',a)
ex = [8,9]
a.extend(ex)
print('a - ',a)

# List 삭제 : del, remove, property
while a:
    l = a.pop()
    print (l is 4)
