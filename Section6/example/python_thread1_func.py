import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# Process : 어떤 작업을 실행할 수 있는 파일, Chrome이나 Exploer (exe file) 등
# Thread : Process 내에서 작동(동작)하는 실행의 최소 단위 _ MainThread

# Multi Thread : 한개의 작업(Process)을 나눠서 진행하기 때문에 Memory를 공유해야함, 공유(자원) -> 여러 흐름을 생성
# Mutli Process : 별개의 메모리 공간 사용
# Process 전환 속도 < Thread 전환 속도, 방법도 더 간단함 (Process의 경우 운영체제에서 Process 간 메모리 공유 시켜야함)

import threading

# Thread 실행 - 함수형
def thread_run():
    print('Thread running - F')

def thread_run_msg(msg):
    print('Thread running - F',msg)

for i in range(1000):
    t1 = threading.Thread(target=thread_run)
    t2 = threading.Thread(target=thread_run_msg, args=('srevice',)) # args 는 tuple 형태로 진행

    t1.start()
    t2.start()
