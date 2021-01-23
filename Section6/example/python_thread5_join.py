import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# Logging Package

import logging
import threading
import time

logging.basicConfig(
    level = logging.DEBUG,
    format = '[%(levelname)s (%(threadName)-8s) %(message)s]', #s : 문자열 , tuple 이기 때문에 ',' 표시
)

def worker1():
    logging.debug('Starting') # levelname = Debug,Info,Fatal 등
    time.sleep(0.5)
    logging.debug('Exiting')

def worker2():
    logging.debug('Starting') # levelname = Debug,Info,Fatal 등
    time.sleep(0.5)
    logging.debug('Exiting')


t1 = threading.Thread(name='service-1', target=worker1)
t2 = threading.Thread(name='service-2', target=worker2 ,daemon=True)
t3 = threading.Thread(target=worker1, daemon=True)

if __name__ == '__main__':
    t1.start()
    t2.start()
    t3.start()

    # join method 호출로 thread 종료시 까지 대기
    # daeon 옵션을 사용하지만, 다끝날때까지 지속 대기
    print('t3 : isAlive()', t3.is_alive()) # 소멸 상태 확인 함수
    t1.join() # join(time) time 동안 대기
    t2.join()
    t3.join()
    print('t3 : isAlive()', t3.is_alive())
