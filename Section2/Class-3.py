import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

# Class - 객체지향
# Class = field(속성 변수) + method(동적-작업을 수행)
# ex) 자동차 -> 속성(색상, 배기량, 자동 등) , Method(전진,후진,왼쪽,오른쪽)

# http://docs.python.org/3/tutorial/classes.html

class selftest:
    def function1():
        print('function1 call!')

    def function2(self):
        print(id(self))
        print('function2 call!')

f = selftest()
print(dir(f))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', .... 'function1', 'function2']

# f.function1() -> function1() takes 0 positional arguments but 1 was given
# f.function2() -> function2 call!

print(id(f)) # 1884152991024
f.function2() # f가 instance로 self 사용했을 때 self로 f를 받음
