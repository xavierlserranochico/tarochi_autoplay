from config import *
import pyautogui
import time


class GameBot:
               
    def get_cursor_position():
        x, y = pyautogui.position()
        print({'X': x, 'Y': y}) 


    def return_to_loop():
        return
     
     
    def move_to(x:int, y:int):
        pyautogui.moveTo(x, y, CURSOR_SPEED-.10)
       
                
    def click(x:int, y:int):
        pyautogui.click(x, y)
        time.sleep(.15)


    def close_window():
        pyautogui.press('q')
        time.sleep(1)


    def move_down(steps:int):
        for _ in range(steps):
            pyautogui.press('s')    
            time.sleep(CLICK_SPEED)