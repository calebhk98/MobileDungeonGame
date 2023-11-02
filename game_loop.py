import pygame
from dungeon import Dungeon
from game_assets import *

# Initialization
pygame.init()

# Setup game objects
dungeon = Dungeon()

# Game Loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

    # Update game states
    dungeon.update()
    
    # Draw or Render
    dungeon.draw()

pygame.quit()