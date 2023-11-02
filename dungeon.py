import random
from random import randint

class Dungeon:

    def __init__(self, settings, assets):
        
         # This constructor initializes all the basic properties of the dungeon.
        # These properties can include initial size, list of existing traps and monsters, growth rate, etc.	    self.size = 0  # represents the initial size of the dungeon
        self.growth_rate = 1  # represents how fast the dungeon grows
        self.traps = []  # holds the existing traps in the dungeon
        self.monsters = []  # holds the existing monsters in the dungeon
        self.rooms=[]
        self.floors=[] #Each floor will have some rooms
        self.size = 0
        self.assets=assets
        self.settings=settings

    # It takes a Pygame surface as an argument, and draws the current state of the dungeon on it.
    # The function will need to loop through all 'tiles' or 'cells' that represent dungeon and draw appropriate graphics (like walls, corridors, traps, monsters, etc.)
    def draw(self, surface):
        # Assuming you have a 2D list or array called 'tiles' containing your dungeon data.
    	# And 'tile_width' and 'tile_height' variables storing the dimensions of each tile.
    	# Also assuming you have a 'tile_image' object which is a Pygame image surface loaded with an image representing a single dungeon tile.

        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[x])):
                if self.tiles[x][y] == 1:  # Assuming '1' represents a dungeon tile in your data.
                    surface.blit(self.tile_image, (x * self.tile_width, y * self.tile_height))
            # This function is responsible for visual representation of the dungeon on game display.

    def grow(self):  
        # This function is called whenever the dungeon needs to grow, i.e., after consuming an adventurer.
        # The growth could be an increase in dungeon size, creation of new corridors, rooms, addition of new traps or monsters, etc.
        # The key part of this function is defining what 'growth' means in your game: More rooms? Stronger traps/monsters? etc.
    
        # we'll define a simple growth mechanism for this function: for now, each growth will simply add a new room to the dungeon.

        # there's a lot of ways you can manage and structure your dungeon, so this is just one of many possible implementations.
        # let's say we have an internal list called self.rooms representing all rooms in the dungeon. Each room can be a dictionary containing its properties.

        # Before adding a room, let's define it.
        new_room = {
            'id': len(self.rooms) + 1,  # The id of the new room is one more than the number of existing rooms.
            'size': random.randint(10, 20),  # Random size between 10 and 20 for this example.
            'traps': [],  # Initially no traps. You can call self.add_trap() here if you want to add a trap immediately to the room.
            'monsters': []  # Initially no monsters. You can call self.add_monster() here if you want to add a monster immediately to the room.
        }

        # Now add the new room to the dungeon.
        self.rooms.append(new_room)

        return new_room  # Return the newly created

    def add_trap(self):
        # This function is used to add a new trap to the dungeon.
        # The trap could be added in a random or predefined location, and its strength or type could also be determined based on the current state of the dungeon.
        
        # Assuming the dungeon is a 2D grid represented by a list of lists
        # We will also assume that each 'cell' of the dungeon grid can either hold a monster, trap, or nothing
        # Grid cells are represented by a dictionary {'monster': MonsterObj,'trap': TrapObj}
        # If a monster or trap doesn't exist in that cell, their value will be None 
        
        trap_added = False
        while not trap_added:
            # Find a random dungeon cell
            x = randint(0, len(self.grid)-1)
            y = randint(0, len(self.grid[0])-1)
            
            # Check if the cell is empty (no monster or trap is in it)
            if self.grid[x][y]['monster'] is None and self.grid[x][y]['trap'] is None:
                # Add a new trap to the cell
                self.grid[x][y]['trap'] = Trap(x,y)
                trap_added = True
    
    def add_monster(self):
        # This function is used to add a new monster to the dungeon.
        # Similar to adding a trap, you'll need to determine where the monster is placed and what its characteristics are.
        # Assuming the dungeon is a 2D grid represented by a list of lists
        # We will also assume that each 'cell' of the dungeon grid can either hold a monster, trap, or nothing
        # Grid cells are represented by a dictionary {'monster': MonsterObj,'trap': TrapObj}
        # If a monster or trap doesn't exist in that cell, their value will be None 
        
        monster_added = False
        while not monster_added:
            # Find a random dungeon cell
            x = randint(0, len(self.grid)-1)
            y = randint(0, len(self.grid[0])-1)
            
            # Check if the cell is empty (no monster or trap is in it)
            if self.grid[x][y]['monster'] is None and self.grid[x][y]['trap'] is None:
                # Add a new trap to the cell
                self.grid[x][y]['monster'] = Monster(x,y)
                monster_added = True

    def collide_with_adventurer(self, adventurer):
        # This function takes an Adventurer object as an argument and checks if there’s a collision between the adventurer and any of the dungeon's traps or monsters.
        # Depending on your game rules, a collision might result in a decrease in the adventurer's health, or their total defeat, which would then call the dungeon's grow() function.
        
        #Need to change this so it only checks monsters and traps in the room the adventurer is in.
        # Collision with monsters
        for monster in self.monsters:
            if adventurer.rect.colliderect(monster.rect):
                # Collision detected. You can define your logic here.
                # For example, reducing adventurer's health and checking if he is defeated
                adventurer.health -= monster.strength
                if adventurer.health <= 0:
                    self.grow() # Dungeon grows if adventurer is defeated
                    return True # You may want your function to return whether the adventurer was defeated

        # Collision with traps
        for trap in self.traps:
            if adventurer.rect.colliderect(trap.rect):
                # Similar to handling monsters collision.
                adventurer.health -= trap.damage 
                if adventurer.health <= 0:
                    self.grow() 
                    return True

        # return False if no collision resulted in a defeat
        return False 
    
    def update(self, growth_increase, defeated_adventurer):
        # Update the dungeon growth and number of defeated adventurers
        self.dungeon_growth += growth_increase
        self.defeated_adventurers += defeated_adventurer
        
        # Call function to check if it's time to level up
        self.check_level_up()

    def check_level_up(self):
        # If growth reaches certain threshold, increase the level
        if self.dungeon_growth >= self.current_level * 10:  # example condition
            self.current_level += 1