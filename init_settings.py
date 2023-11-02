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

#    def game_loop(self, game_window):
#        running = True
#        while running:
#            for event in pygame.event.get():
##                if event.type == pygame.QUIT:
#                    # pygame window is closed by user
#                    running = False
#            
#            game_window.fill((00,55,00))
#            # update the display
#            pygame.display.flip()
#
#        # If you get here, your user has exited, so you can close everything:
#        pygame.quit()