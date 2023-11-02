class GameState:
    def __init__(self):
        # Initialize the game state
        self.dungeon_growth = 0
        self.defeated_adventurers = 0
        self.current_level = 1
        self.game_over = False
        self.menu_showing=True
        self.game_running = True
        

    

    def check_game_over(self):
        # Define game over condition
        if self.dungeon_growth >= 100:  # example condition
            self.game_over = True
            # Handle game_over situation here