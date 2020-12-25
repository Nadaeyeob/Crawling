import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

# Class - 객체지향
# Class = field(속성 변수) + method(동적-작업을 수행)
# ex) 자동차 -> 속성(색상, 배기량, 자동 등) , Method(전진,후진,왼쪽,오른쪽)

# http://docs.python.org/3/tutorial/classes.html

# Class 변수, Instance 변수

class nametest:
    total = 0

print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'io', 'nametest', 'sys']
print('before',nametest.__dict__)
nametest.total = 1
print('after',nametest.__dict__)

n1 = nametest()
n2 = nametest()

print(id(n1),'vs',id(n2))
print(dir()) # ['__annotations__', ... 'io', 'n1', 'n2', 'nametest', 'sys']
print(n1.__dict__)
print(n2.__dict__) # -> null 로 나옴
n1.total = 77
print(n1.__dict__) # -> total(key) 77(value)로 저장
print(n1.total) # -> n1에 저장된 77 반환
print(n2.total) # -> class 변수인 1 반환
