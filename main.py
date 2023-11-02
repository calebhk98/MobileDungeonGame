import pygame
import init_settings
import game_assets
import dungeon
import event_handling
import screen_updates
import collision_detection
import game_state
import game_screens
from menu import Menu

class LivingDungeonGame:
    def __init__(self):
        pygame.init()
        self.settings = init_settings.Settings()
        self.assets = game_assets.Assets()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.state = game_state.GameState()
        self.game_menu = Menu(self.settings, self.assets)

    def run_game(self):
        while True:
            if self.state.menu_showing:
                self._show_menu()
            else:
                self._game_loop()

    def _show_menu(self):
        self.game_menu.render(self.screen)
        pygame.display.update()
        event_handling.check_menu_events(self.game_menu, self.state)

    def _game_loop(self):
        dun = dungeon.Dungeon(self.settings, self.assets)
        while self.state.game_running:
            self._handle_events(dun)
            self._check_collisions(dun)
            self._update_game_state(dun)
            self._update_screen(dun)

        game_screens.display_end_screen(self.settings, self.assets, self.state)

    def _handle_events(self, dun):
        event_handling.handle_events()

    def _check_collisions(self, dun):
        pass
        #collision_detection.check_collisions(dun)

    def _update_game_state(self, dun):
        pass
        #self.state.update_state(dun)

    def _update_screen(self, dun):
        pass
        #screen_updates.update()


if __name__ == "__main__":
    game = LivingDungeonGame()
    game.run_game()
