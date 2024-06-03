from conditional import Condition
from config import *
import pyautogui
import random
import time

class FightMoves:

    def flight(game_state):
        # Loop to press the space key four times
        for _ in range(5):
            #print(_)
            pyautogui.press('space')
            # Add a short delay between each key press (optional)
            time.sleep(random.uniform(0.55, 0.65))
        
        # Wait for Battle Animation to end
        for i in range(SECONDS, 0, -1):
            time.sleep(1) 

            # Print Game Mode Related Attributes
            if game_state.game_mode == 'farm':
                print("--------------------------")
                print(i)  
                print()
                Condition.is_health_low(game_state, player=1)
                print(game_state.is_health_low, game_state.item)
                print()  
            else:   
                print(i)
            
            # Return to Flight
            if Condition.is_attack_available():
                print("?")
                return

            # Quit Loop if fight is over
            if Condition.is_battle_result_available():
                print("??")
                # Set This for Arena Mode Only
                if game_state.game_mode == 'arena':
                    game_state.is_arena_fight_complete = True
                time.sleep(2)
                return
            
            # Emergency Escape?
            if i == 1:
                print("???")
                return

    def capture(game_state):
        
        # Loop to press the space key four times
        for _ in range(5):
            #print(_)
            pyautogui.press('space')
            # Add a short delay between each key press (optional)
            time.sleep(random.uniform(0.45, 0.65))
        
        # Wait for Battle Move to end
        for i in range(SECONDS, 0, -1):
            time.sleep(1)            
            print("--------------------------")
            print(i)  
            print()
            
            # Checks the status of health
            health_low, item = Condition.is_health_low(game_state, player=2)
            print(health_low, item)
            print()  
            
            # Capture Monster
            while health_low == True:
                print('Capture?')
                
                return False, None
                
                
            # Return to Flight
            if Condition.is_attack_available():
                print("?")
                return False, None    

            # Quit Loop if fight is over
            if Condition.is_battle_result_available():
                print("??")
                time.sleep(2)
                return health_low, item
            
            