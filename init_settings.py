import pygame

class Settings:
    def __init__(self):
        pygame.init()
        self.screen_width = 1024
        self.screen_height = 768
        game_window = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.set_game_title('My Pygame Window')
#        self.game_loop(game_window)  
    
    def set_game_title(self, title):
        pygame.display.set_caption(title)

