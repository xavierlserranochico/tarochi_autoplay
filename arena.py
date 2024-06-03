from conditional import Condition
from moves import FightMoves
from game_bot import GameBot
from menu import Menu
from config import *
import pyautogui


class Arena:
    
    def enter_tarochi_arena():
        # Enter Arena
        print('Arena Time Babbyyyy!!')
        pyautogui.press('space')
        time.sleep(2)
        
    def close_tarochi_arena():
        # Close Arena
        pyautogui.press('q')
        time.sleep(1)
        
    def enter_arena(game_state):
        # Select the Arena
        print('Lets goo!')
        print()
        if game_state.arena == 'BRONZE':
            pyautogui.press('space')
        elif game_state.arena == 'SILVER':
            GameBot.move_down(1)
            pyautogui.press('space')      
        elif game_state.arena == 'GOLD':
            GameBot.move_down(2)
            pyautogui.press('space')
        elif game_state.arena == 'PLATINUM':
            GameBot.move_down(3)
            pyautogui.press('space')
        elif game_state.arena == 'DIAMOND':
            GameBot.move_down(4)
            pyautogui.press('space')
        else:
            print('Error: No Arena provided')
        # Wait for Arena To load
        time.sleep(13)
  
    def swap_team(game_state, arena:str):
            
        # Set Arena
        game_state.arena = arena
            
        # Close Arena Window
        GameBot.close_window()
            
        # Open Menu
        Menu.open_menu()
            
        # Enter Team & Items
        pyautogui.press('e')
        time.sleep(MENU_SPEED)
            
        # Enter Items Tab
        pyautogui.press('s')
        time.sleep(MENU_SPEED)
            
        # Swap first slot
        for _ in range(3):
            if _ == 0:
                pyautogui.press('space')
                time.sleep(MENU_SPEED)
                    
                pyautogui.press('space')
                time.sleep(MENU_SPEED)
                
                pyautogui.press('s')
                time.sleep(MENU_SPEED)
            
                pyautogui.press('space')
                time.sleep(MENU_SPEED)
                    
                time.sleep(SWAP_SPEED)            
            elif _ == 1:
                pyautogui.press('s')
                time.sleep(MENU_SPEED)

                pyautogui.press('d')
                time.sleep(MENU_SPEED)
                                
                pyautogui.press('space')
                time.sleep(MENU_SPEED)

                pyautogui.press('space')
                time.sleep(MENU_SPEED)

                pyautogui.press('s')
                time.sleep(MENU_SPEED)
                
                pyautogui.press('space')
                time.sleep(MENU_SPEED)
                                                           
                time.sleep(SWAP_SPEED)            
            elif _ == 2:
                pyautogui.press('s')
                time.sleep(MENU_SPEED)

                pyautogui.press('d')
                time.sleep(MENU_SPEED)

                pyautogui.press('d')
                time.sleep(MENU_SPEED)

                pyautogui.press('space')
                time.sleep(MENU_SPEED)

                pyautogui.press('space')
                time.sleep(MENU_SPEED)

                pyautogui.press('s')                    
                time.sleep(MENU_SPEED)

                pyautogui.press('space')
                time.sleep(MENU_SPEED)
                                                           
                time.sleep(SWAP_SPEED)  
        
    def lets_get_ready_to_rumble(game_state):
        
        # Talk to the guy to enter Arena
        Arena.enter_tarochi_arena()
        
        # If Arena Available
        if Condition.is_arena_conquered('BRONZE') and Condition.is_teamate_champion('BRONZE'):
            
            # Team Changes if necesary 
            if game_state.arena != 'BRONZE':
                Arena.swap_team(game_state, 'BRONZE')

            # Enter Bronze Arena
            Arena.enter_arena(game_state)
            
            # Loop Until Fight is Complete
            while game_state.is_arena_fight_complete == False:
                
                # Check if attact is available
                if Condition.is_attack_available():
                    FightMoves.flight(game_state)
                        
                time.sleep(1)
            
            # Reset Arena Flag for Next Round 
            game_state.is_arena_fight_complete = False
            
            # Close Window
            GameBot.close_window()
            time.sleep(9)            
        elif Condition.is_arena_conquered('SILVER') and Condition.is_teamate_champion('SILVER'):

            # Team Changes if necesary 
            if game_state.arena != 'SILVER':
                Arena.swap_team(game_state, 'SILVER')

            # Enter Platinum Arena
            Arena.enter_arena(game_state)
            
            # Loop Until Fight is Complete
            while game_state.is_arena_fight_complete == False:
                
                # Check if attact is available
                if Condition.is_attack_available():
                    FightMoves.flight(game_state)
                        
                time.sleep(1)
            
            # Reset Arena Flag for Next Round 
            game_state.is_arena_fight_complete = False
            
            # Close Window
            GameBot.close_window()
            time.sleep(9)  
        elif Condition.is_arena_conquered('PLATINUM') and Condition.is_teamate_champion('PLATINUM'):
            
            # Team Changes if necesary 
            if game_state.arena != 'PLATINUM':
                Arena.swap_team(game_state, 'PLATINUM')

            # Enter Platinum Arena
            Arena.enter_arena(game_state)
            
            # Loop Until Fight is Complete
            while game_state.is_arena_fight_complete == False:
                
                # Check if attact is available
                if Condition.is_attack_available():
                    FightMoves.flight(game_state)
                        
                time.sleep(1)
            
            # Reset Arena Flag for Next Round 
            game_state.is_arena_fight_complete = False
            
            # Close Window
            GameBot.close_window()
            time.sleep(9)          
            
            
        else:
            print('We Champs Baby!')
            Arena.close_tarochi_arena()
            # Wait a Little for someone to win / Adjust if needed
            time.sleep(15)
            print()