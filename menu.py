from game_bot import GameBot
from config import *
import pyautogui
import time


class Menu:
    
    def open_menu():
        # Open Menu
        pyautogui.press('tab')
        time.sleep(1)
        
    def hp_potion():
        print('HP Potion')
        
        # Quit the fight thingy 
        pyautogui.press('q')
        
        # Open Menu
        Menu.open_menu()
        
        # Enter Team & Items
        pyautogui.press('e')
        time.sleep(MENU_SPEED)
        
        # Enter Items Tab
        pyautogui.press('d')
        time.sleep(MENU_SPEED)
        
        # Loop to press the space key four times
        for _ in range(5):
            pyautogui.press('s')
            # Add a short delay between each key press (optional)
            time.sleep(CLICK_SPEED)
            
        # Hopefully Select the HP MAX lol
        pyautogui.press('d')
        time.sleep(CLICK_SPEED)
               
        # Heal First Monster
        pyautogui.press('e')
        time.sleep(CLICK_SPEED)
        pyautogui.press('e')
        time.sleep(CLICK_SPEED)
        pyautogui.press('e')
            
    def max_hp_potion():
        print('Max HP Potion')
        
        # Quit the fight thingy 
        pyautogui.press('q')
        
        # Open Menu
        Menu.open_menu()
        
        # Enter Team & Items
        pyautogui.press('e')
        time.sleep(MENU_SPEED)
        
        # Enter Items Tab
        pyautogui.press('d')
        time.sleep(MENU_SPEED)
        
        # Loop to press the space key four times
        for _ in range(4):
            pyautogui.press('s')
            # Add a short delay between each key press (optional)
            time.sleep(CLICK_SPEED)
        
        # Hopefully Select the HP MAX lol
        pyautogui.press('d')
        time.sleep(CLICK_SPEED)
        
        # Heal First Monster
        pyautogui.press('e')
        time.sleep(CLICK_SPEED)
        pyautogui.press('e')
        time.sleep(CLICK_SPEED)
        pyautogui.press('e')
             
    def monster_attraction():
        print('Monster Attraction Card')
         
        # Check To Stop Process
        if GameBot.is_fight_available():
            GameBot.return_to_loop()
        
        # Quit the fight thingy 
        pyautogui.press('q')
         
        # Check To Stop Process
        if GameBot.is_fight_available():
            GameBot.return_to_loop()        
        
        # Open Menu
        Menu.open_menu()
        
        # Check To Stop Process
        if GameBot.is_fight_available():
            GameBot.return_to_loop()        
        
        # Enter Team & Items
        pyautogui.press('e')
        time.sleep(MENU_SPEED)
        
        # Check To Stop Process
        if GameBot.is_fight_available():
            GameBot.return_to_loop()        
        
        # Enter Items Tab
        pyautogui.press('d')
        time.sleep(MENU_SPEED)
        
        # Check To Stop Process
        if GameBot.is_fight_available():
            GameBot.return_to_loop()        
        
        # Loop to press the space key four times
        for _ in range(4):
            pyautogui.press('s')
            # Add a short delay between each key press (optional)
            time.sleep(CLICK_SPEED)
        
        # Check To Stop Process
        if GameBot.is_fight_available():
            GameBot.return_to_loop()                   
        
        # Use Monster Attraction
        pyautogui.press('e')

