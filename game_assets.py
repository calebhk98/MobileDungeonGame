import pygame


class Assets:
    def __init__(self):
        # Initialize Pygame mixer for sound loading
        pygame.mixer.init()
        self.load_images()
        self.load_sounds()
    

    def load_images(self):
        self.images = {
            #"dungeon": pygame.image.load('path/to/dungeon_sprite.png'),
            #"adventurer": pygame.image.load('path/to/adventurer_sprite.png'),
            #"trap": pygame.image.load('path/to/trap_sprite.png'),
            #"monster": pygame.image.load('path/to/monster_sprite.png'),
        }

    def load_sounds(self):
        self.sounds = {
            #"growth": pygame.mixer.Sound('path/to/growth_sound.wav'),
            #"trap": pygame.mixer.Sound('path/to/trap_sound.wav'),
            #"monster": pygame.mixer.Sound('path/to/monster_sound.wav'),
        }

    def get_image(self, name):
        return self.images[name]

    def get_sound(self, name):
        return self.sounds[name]