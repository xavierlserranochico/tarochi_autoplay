from game_state import GameState, ValidationError
from image import ImageProcessingv2
from conditional import Condition
from game_bot import GameBot
from arena import Arena
from config import *
import time


# Initialize Game Variables
#game_state = GameState()
#game_state.game_mode = GAME_MODE



#Condition.is_arena_conquered('BRONZE')

#Arena.swap_team(game_state, 'BRONZE')


#GameBot.get_cursor_position()
Condition.is_teamate_champion('DIAMOND')
Condition.is_arena_conquered('DIAMOND')