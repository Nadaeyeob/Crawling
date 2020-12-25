import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

# Class - 객체지향
# Class = field(속성 변수) + method(동적-작업을 수행)
# ex) 자동차 -> 속성(색상, 배기량, 자동 등) , Method(전진,후진,왼쪽,오른쪽)

# http://docs.python.org/3/tutorial/classes.html

# Class 변수, Instance 변수

class warehouse:
    stock_num = 0
    def __init__(self,name):
        self.name = name # Instance 변수 self 사용
        warehouse.stock_num+=1

    def __del__(self):
        warehouse.stock_num-=1

user1 = warehouse('kim')
user2 = warehouse('park')

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__) # stock_num 이 보이지 않음

print(warehouse.__dict__) # stock_num = 2 Instance namespace -> class namespace 를 찾음, Class 변수는 공유됌
print(user1.stock_num) # 2
print(user2.stock_num) # 2 -> Instance 변수는 자기 자신만 가지나, Class 변수는 공통적으로 받음
