import pygame

# Assuming 'screen' is your game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Game Over Function
def game_over_screen():
    font = pygame.font.Font(None, 74) # Choose your preferred font and size
    text = font.render("GAME OVER", 1, (255, 0, 0)) # Here, (255,0,0) is the RGB color value for Red
    screen.blit(text, (250,250)) # Change the coordinates as per your layout
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.update()