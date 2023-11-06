### Project Overview:

- **LivingDungeonGame (main.py) (initialization inputs)**
  - *Initializes the game environment and variables.*
  - Methods:
    - run_game(): Starts the main game loop.
    - _show_menu(): Displays the game's main menu.
    - _game_loop(): The core loop that runs every frame of the game.
    - _handle_events(events): Processes player inputs and game events.
    - _check_collisions(): Detects and handles collisions between game objects.
    - _update_game_state(): Updates the state of the game based on current events.
    - _update_screen(): Renders the current state to the screen.
    - quit_game(): Safely exits the game, performing any necessary cleanup.

- **Dungeon (dungeon.py) (settings, assets)**
  - *Manages the dungeon's structure and interactions within the game.*
  - Methods:
    - draw(surface): Draws the dungeon on the Pygame surface.
    - grow(): Expands the dungeon's size or complexity.
    - add_trap(trap): Adds a trap to the dungeon's traps list.
    - add_monster(monster): Adds a monster to the dungeon's monsters list.
    - collide_with_adventurer(adventurer): Checks for and handles collisions with adventurers.
    - update(): Updates the dungeon state, such as monster movements.
    - check_level_up(): Checks if the dungeon meets the criteria to level up.

- **EventBus (event_bus.py) ()**
  - *Handles the event dispatching system, allowing for a publish-subscribe pattern in the game.*
  - Methods:
    - register(event_type, listener): Registers a listener for a specific type of event.
    - dispatch(event): Dispatches an event to the appropriate listeners.

- **GameOverEvent (event_handling.py) ()**
  - *Represents a game over event.*

- **QuitEvent (event_handling.py) ()**
  - *Represents an event to quit the game.*
  - Methods:
    - handle_events(event): Handles events that are related to quitting the game.
    - check_menu_events(menu): Checks and handles events occurring in the game menu.

- **Assets (game_assets.py) (asset_folder)**
  - *Manages the loading and retrieval of game assets like images and sounds.*
  - Methods:
    - load_images(): Loads images into the game from the specified folder.
    - load_sounds(): Loads sounds into the game from the specified folder.
    - get_image(name): Retrieves an image asset by name.
    - get_sound(name): Retrieves a sound asset by name.

- **GameState (game_state.py) ()**
  - *Manages the overarching state of the game, such as checking for game over conditions.*
  - Methods:
    - check_game_over(): Evaluates whether the game has reached an end state.
    - handle_quit(): Manages the process of quitting the game, like saving progress.

- **Settings (init_settings.py) ()**
  - *Configures initial settings for the game, such as the game title.*
  - Methods:
    - set_game_title(title): Sets the game's title.

- **Button (menu.py) (text, position)**
  - *Initializes a button UI element.*
  - Methods:
    - render(surface): Draws the button to the screen.
    - was_touched(touch_position): Checks if the button was interacted with.

- **Menu (menu.py) (options)**
  - *Sets up a menu with various selectable options.*
  - Methods:
    - render(surface): Displays the menu options on the screen.
    - check_for_touch(touch_position): Determines if a menu option was selected.
    - select_option(option): Executes the action associated with a selected option.
    - navigate_to(menu_item): Goes to a different menu screen.
    - navigate_back(): Returns to the previous menu screen.

- **Screen (screen_updates.py) (display_surface)**
  - *Creates a screen object to manage visuals.*
  - Methods:
    - draw_dungeon(dungeon): Renders the dungeon layout to the display.
    - update(): Refreshes the screen to reflect any changes.
   
- **(collision_detection.py) (object1, object2)**
  - *returns true if the 2 collide.*
 
- **(event_handling.py)**
  - *Handles Events.*
  - Methods:
    - handle_events(event): Handles events that are related to quitting the game.
    - check_menu_events(menu): Checks and handle

