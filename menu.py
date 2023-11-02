import pygame

class Button:
    def __init__(self, text, position):
        self.text = text
        self.position = position   # position should be a tuple (x, y)
        self.width = 250   # You can adjust these parameters as needed
        self.height = 50
        self.color = (255,255,0)

    def render(self, screen, assets):
        """Render the button to the screen."""
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.width, self.height))

        # Assuming assets include a predefined font
        try:            
            k=2
            font = pygame.font.Font(None, 36)  # Using default font with size 36
            text_surf = font.render(self.text, True, (0, 0, 0))  # Black text color
            text_rect = text_surf.get_rect(center=(self.position[0] + self.width // 2, self.position[1] + self.height // 2))
            screen.blit(text_surf, text_rect.topleft)
        except Exception as e:
            print(f"Error in Button render: {str(e)}")

    def was_touched(self, touch_position):
        """Returns True if the button was touched, False otherwise."""
        x, y = touch_position
        button_x, button_y = self.position

        return (button_x <= x <= button_x + self.width) and (button_y <= y <= button_y + self.height)
    
    

class Menu:
    def __init__(self, settings, assets):
        self.settings = settings
        self.assets = assets
        self.buttons = []  # We'll use buttons instead of options for touch controls
        self.current_menu = 'main'  # Default to main menu
        self.menu_stack = []  # Stack to handle sub-menus

        button_texts = ["Start New Game", "Load Game", "Settings"]
        for index, text in enumerate(button_texts):
            # Create a new button for each option
            # The Button class doesn't exist yet – you'll need to create it!
            new_button = Button(text, position=(100, 100 + index * 60))  # Adjust position as needed
            self.buttons.append(new_button)

    def render(self, screen):
        """Render the menu on the screen."""
        if self.current_menu == 'main':
            for button in self.buttons:
                button.render(screen, self.assets)
        elif self.current_menu == 'sub_menu_name':  # Replace 'sub_menu_name' with your submenu's name
            # Render the buttons for this sub-menu
            pass
        pygame.display.flip()


    def check_for_touch(self, position, state):
        """Check whether a menu option was touched."""
        for button in self.buttons:
            if button.was_touched(position):
                if button.text == "Settings":  # If 'Settings' button is touched
                    self.navigate_to('settings')  # Navigate to the 'settings' sub-menu
                else:
                    self.select_option(state, button)


    def select_option(self,state, button):
        print(button.text)
        """Perform an action based on the touched button."""
        if button.text == "Start New Game":
            state.menu_showing=False
            pass  # Implement functionality here
        elif button.text == "Load Game":
            pass  # Implement functionality here
        elif button.text == "Settings":
            pass  # Implement functionality here
    
    def navigate_to(self, menu_name):
        self.menu_stack.append(self.current_menu)
        self.current_menu = menu_name

    def navigate_back(self):
        if self.menu_stack:
            self.current_menu = self.menu_stack.pop()

