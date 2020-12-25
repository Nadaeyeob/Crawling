import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding= 'utf-8')

# Class - 객체지향
# Class = field(속성 변수) + method(동적-작업을 수행)
# ex) 자동차 -> 속성(색상, 배기량, 자동 등) , Method(전진,후진,왼쪽,오른쪽)

# http://docs.python.org/3/tutorial/classes.html

class userinfo:
    def set_info(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print('---')
        print('name:'+self.name)
        print('phone:'+self.phone)
        print('---')

user1 = userinfo()
user2 = userinfo()

print(id(user1)) #1821513090288
print(id(user2)) #1821513092496

user1.set_info('kim','010-1234-5678')
user2.set_info('park','010-2345,6789')

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)

# dic 형태로 저장되어 user1.name 으로 호출 가능함
print(user1.name)
