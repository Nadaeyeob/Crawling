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

# DEMONTHREAD : (옵션 생략 시 기본 Thread)
# Main이 끝나면 자동으로 Thread 종료
t1 = threading.Thread(name='service-1', target=worker1)
t2 = threading.Thread(name='service-2', target=worker2, daemon=True)
t3 = threading.Thread(target=worker1, daemon=True)

# name을 지정하지 않을 경우 (t3)
# [DEBUG (Thread-1) Starting]
# [DEBUG (Thread-1) Exiting]

t1.start()
t2.start()
t3.start()

# 위와 같은 내용
# if __name__  == '__main__'
#     t1.start()
#     t2.start()
#     t3.start()
