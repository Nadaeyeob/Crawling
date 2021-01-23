import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 지속 실행되게 하는 (일정시간 간격 반복 실행) 하는 Code (Thread 사용)
import time
import threading

def thread_run():
    print('======',time.ctime(),'======')
    # 개발하고자 하는 코드 작성

    ############################################
    for i in range(1,10000):
        print('Threading running - ',i)
    ############################################

    threading.Timer(2.5,thread_run).start() # 재귀함수
    # threading.Timer(s) _ int로 하여 진행

thread_run()
