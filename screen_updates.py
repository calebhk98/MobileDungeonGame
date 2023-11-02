import pygame

class Screen:
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))

    def draw_dungeon(self, dungeon): 
        # Here, add the logic to draw your dungeon
        pass 

    def update(self):
        pygame.display.flip()