import pygame
import sys

class GameOverEvent:
    pass
class QuitEvent:
    pass

def handle_events(event_bus):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            event_bus.dispatch(QuitEvent())

        # you can add other types of events such as MOUSEBUTTONDOWN, KEYDOWN etc.
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_UP:
                print("Up arrow key was pressed")
            elif event.key == pygame.K_DOWN:
                print("Down arrow key was pressed")

        # For touch events, you would need to track MOUSEBUTTONDOWN and MOUSEBUTTONUP events
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(f"You touched the screen at {pos}")
    return True

def check_menu_events(game_menu, state, event_bus):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                event_bus.dispatch(QuitEvent())

        # For touch events, you would need to track MOUSEBUTTONDOWN and MOUSEBUTTONUP events
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            game_menu.check_for_touch(pos, state)  # in main.py where menu is an instance of Menu
    return True
