# Sets 집합자료형 (순서x, 중복x) -> List나 Tuple로 바꿔서 사용해야함(indexing 등 모두 불가)
# 사용하기 좋은 Method 때문에 사용

a = set()
b = set([1,2,3,4])

print(type(b))
print(b) # {1, 2, 3, 4}

t = tuple(b)
print(type(t),t)
print(t[0:2]) # (1, 2)

l = list(b)
print(type(l),l)
print(l[0:2]) # [1, 2]

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print('t - ', s1 & s2)
print('t - ', s1.intersection(s2))

print('t - ', s1 | s2)
print('t - ', s1.union(s2))

s3 = set([0,1,2,3])
s3.add(4)
print(s3)
s3.remove(2)
print(s3)
