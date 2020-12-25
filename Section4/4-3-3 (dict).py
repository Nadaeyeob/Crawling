# Dictionary 자료형 (key, Value) -> (순서x, 중복x, 수정o, 삭제o)

# 선언
a = {'name' : 'kim','phone' : '010', 'birth' : 920307}
b = {0 : 'hello'}
c = {'arr' : [0,1,2,3]}
print(type(a),a)

# 출력
print('a - ',a['name']) # 존재하지 않을 경우 Error(예외)
print('a - ',a.get('name')) # 존재하지 않을 경우 None 반환
print('c - ',c.get('arr'),type(c.get('arr')))

# 추가
a['address'] = 'seoul'
print('a - ',a)
a['rank'] = [1,2,3]
print('a - ',a)

print('a -', a.keys(),type(a.keys()))
print('a -', list(a.keys()),type(list(a.keys())))

print('a -', a.values(),type(a.values()))
print('a -', list(a.values()),type(list(a.values())))

print('a -', a.items()) # -> tuple 형태로 전환
print('a -', list(a.items())[1])
print('a -', type(list(a.items())[1])) # list 전환해도 Tuple 이다

print('a -', 'name' in a)
print('a -', 'city' in a) # False -> key 값이 없음
