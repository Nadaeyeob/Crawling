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
t2 = threading.Thread(name='service-2', target=worker2)
t3 = threading.Thread(target=worker1)
t4 = threading.Thread(target=worker2)

# name을 지정하지 않을 경우 (t3)
# [DEBUG (Thread-1) Starting]
# [DEBUG (Thread-1) Exiting]

t1.start()
t2.start()
t3.start()
t4.start()
