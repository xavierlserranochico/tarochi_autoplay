from game_state import GameState, ValidationError
from conditional import Condition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
from moves import FightMoves
from arena import Arena
from menu import Menu
from misc import Misc  
from config import *
import time


def main():
    try:
        # Initialize Game Variables
        game_state = GameState()
        game_state.game_mode = GAME_MODE

        while True:
            # Check the Game Mode // You Can Change it in the Config file
            if game_state.game_mode == 'farm':
                # Check if Fight is available   
                if Condition.is_fight_available():                
                    print(f'Y - Round: {game_state.round_counter}')
                    
                    # Wait for the game to load
                    if game_state.round_counter == 1:
                        time.sleep(3)
                                        
                        # Check if on Capture List
                        Condition.is_on_capture_list(game_state)

                    # Check to see if the Monster is on Catch List     
                    if not game_state.is_on_catch_list:    
                        # Attack Enemy
                        print('Attacckkkkk!!')
                        FightMoves.flight(game_state)
                    else:            
                        # Try Catching Monster
                        print('Catch This!!')
                        FightMoves.flight(game_state)
                                    
                    # Add Round to counter
                    game_state.round_counter += 2                   
                else:
                    # Heal First Monster
                    if game_state.is_health_low:
                        print('Heal Motherfucker!!')
                        # Select the Potion needed based on health percent     ** Doing 1 first 
                        if game_state.item == 'max_hp_potion':
                            Menu.max_hp_potion()
                            
                        game_state.is_health_low = False
                        game_state.item = None
                                
                    # Check if Monster Attraction is Active ** Not In Use at the moment :)
                    if not Condition.is_monster_attraction_active() and Misc.check_date(game_state.run_time):
                        pass
                        #print('Using Monster Attraction Card')
                        
                        # Use Monster Attraction
                        #Menu.monster_attraction()
                        
                        # Update Run Time
                        #RUN_TIME = datetime.now()
                                    
                    # Clear Percent List 
                    game_state.clear_percent_list()
                    
                    # Reset Round Counter
                    game_state.reset_round_counter()

                    print('N')               
            elif game_state.game_mode == 'arena':
                Arena.lets_get_ready_to_rumble(game_state)
            else:
                print('Error: Please Select a Game Mode')
                        
            time.sleep(1)
             
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\nExiting...")
        # Perform cleanup actions if needed

if __name__ == '__main__':
    main() 