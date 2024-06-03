from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import List, Optional
from datetime import datetime


class GameState(BaseModel):
    game_mode: Optional[str] = Field(None, description="Selected Game Mode by the player")
    
    is_health_low: bool = Field(False, description="is Health low must be True or False")
    is_on_catch_list: bool = Field(False, description="if On catch list then True else False")
    
    is_arena_fight_complete: bool = Field(False, description="if True the match is complete else False")
    arena: Optional[str] = Field('PLATINUM', description="Current Arena Playing")
    
    item: Optional[str] = Field(None, description="Item use by the player")
    alt_percent: List[float] = Field(default_factory=list, description="List of alternative percentages")
    run_time: Optional[datetime] = Field(None, description="The start time of the run")
    round_counter: int = Field(1, description="Current round counter")
    capture_card: int = Field(2, description="Tracks the number of capture cards available")
    
    
    
    
    def update_health(self, new_health: int):
        self.is_health_low = new_health
    
    def use_item(self, item):
        self.item = item
        
    def start_timer(self):
        self.run_time = datetime.now()

    def clear_percent_list(self):
        self.alt_percent.clear()
        
    def reset_round_counter(self):
        self.round_counter = 1


    
    @model_validator(mode='before')
    def auto_start_timer(cls, values):
        if 'run_time' not in values or values['run_time'] is None:
            values['run_time'] = datetime.now()
        return values





"""
# Example usage
try:
    game_state = GameState()
    print(game_state)

    # Update health
    game_state.update_health(True)
    print("Updated health:", game_state.is_health_low)

    # Use item
    game_state.use_item('max_hp_potion')
    print("Used item:", game_state.item)

except ValidationError as e:
    print(e.json())
"""

