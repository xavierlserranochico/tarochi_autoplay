from game_state import GameState, ValidationError
from image import ImageProcessingv2
from  moves import Move
from conditional import Condition
from game_bot import GameBot
from config import *
import time



# Initialize Game Variables
game_state = GameState()
#print(json.dumps(json.loads(game_state.json()),indent=4))

while True:
    # Check if Fight is available   
    if Condition.is_fight_available():                
        print(f'Y - Round: {game_state.round_counter}')
                
        # Wait for the game to load
        if game_state.round_counter == 1:
            time.sleep(3)               
                                    
            # Check if on Capture List
            Condition.is_on_capture_list_v2(game_state)
            
        # Check to see if the Monster is on Catch List     
        if game_state.is_on_catch_list:    
            # Try Catching Monster
            print('Catch This!!')
            game_state.is_health_low, game_state.item = Move.capture(game_state)
        else:            
            # Attack Enemy
            print('Attacckkkkk!!')
            game_state.is_health_low, game_state.item = Move.flight(game_state)

        # Add Round to counter
        game_state.round_counter += 2      
                    
    else:
        break
    
                    
