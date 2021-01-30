from PIL import ImageGrab
import time
import keyboard

def screenshot():
    curr_time = time.strftime('_%Y%m%d_%H%M%S')
    img = ImageGrab.grab()
    img.save('C:/Users/sw991/OneDrive/Desktop/Crawling/Image{}.png'.format(curr_time))

keyboard.add_hotkey('F9',screenshot)

keyboard.wait('esc') # 사용자가 esc 누를 때까지 프로그램 실행
