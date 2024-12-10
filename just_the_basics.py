"""
COMMENTS!!!
Comments are lines of code that are *not* executed by the computer. They are just used to explain what the code does.
There are two types of comments in Python:
1. Single-line comments: These comments start with a '#' symbol and continue until the end of the line.
2. Multi-line comments: These comments are enclosed in triple quotes (like the kind you're looking at now!) and can span multiple lines.

Code comments are super useful for explaining what your code does, how it works, and why you wrote it a certain way. Without 
comments, it can be hard to understand code, especially if you come back to it after a long time. So, always remember to comment your code!

Commenting also has another use: you can "comment out" lines of code that you don't want to run. This is useful for debugging or testing. As we 
go through the code, you'll see some lines commented out. This means they won't run when the program is executed.

As an exercise, add your own comments to the code below to explain what each part does. You can also try uncommenting some lines to see what happens!
"""

# First, we need to import the Pygame library and the sys module to handle exiting the game.
# Libraries are collections of functions and methods that allow you to perform many actions without writing the code from scratch.
# We'll go over libraries in more detail later on, but for now, just know that Pygame is a library that helps you create games in Python.
import pygame
import sys
import menu

# "Initialize" Pygame modules. This means that the Pygame library we just imported above
# will set up the necessary components to run the game.
pygame.init()

# Set up the game window dimensions. The SCREEN_WIDTH and SCREEN_HEIGHT variables define the size of the game window.
"""
VARIABLES!!!
We're about to assign our game's very first variables. Variables are 'containers' for storing data values.
In this case, we're storing the width and height of the game window in the variables SCREEN_WIDTH and SCREEN_HEIGHT.
This way, we can easily change the window size later on without having to update multiple places in the code. Neat, right?

Variables are created by assigning a value to a name using the '=' sign. 
Here are the rules for naming variables in Python:
1. A variable name must start with a letter or the underscore character.
2. A variable name cannot start with a number.
3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _).
4. Variable names are case-sensitive (myVar, myvar, and MYVAR are all different variables).
5. Variable names should be descriptive (it helps you and others understand what the code does).
"""
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Top-Down Adventure Game")

# Define player attributes.
PLAYER_SPEED = 5


# Define the Player class inheriting from pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        # Load the sprite sheet image
        sprite_sheet = pygame.image.load(
            "game assets/graphic_assets/character.png"
        ).convert_alpha()

        # Define sprite dimensions, in pixels, on the "character.png" sprite sheet. These values are specific to the sprite sheet used.
        self.sprite_width = 16
        self.sprite_height = 32
        self.animation_speed = 0.1  # Adjust for animation speed

        # Dictionaries to hold animation frames for each direction
        self.animations = {"down": [], "left": [], "right": [], "up": []}

        # Load frames for each direction
        for i in range(4):  # Assuming 4 frames per direction
            # Moving Down
            rect = pygame.Rect(
                i * self.sprite_width, 0, self.sprite_width, self.sprite_height
            )
            self.animations["down"].append(sprite_sheet.subsurface(rect))
            # Moving Left
            rect = pygame.Rect(
                i * self.sprite_width,
                self.sprite_height * 3,
                self.sprite_width,
                self.sprite_height,
            )
            self.animations["left"].append(sprite_sheet.subsurface(rect))
            # Moving Right
            rect = pygame.Rect(
                i * self.sprite_width,
                self.sprite_height,
                self.sprite_width,
                self.sprite_height,
            )
            self.animations["right"].append(sprite_sheet.subsurface(rect))
            # Moving Up
            rect = pygame.Rect(
                i * self.sprite_width,
                self.sprite_height * 2,
                self.sprite_width,
                self.sprite_height,
            )
            self.animations["up"].append(sprite_sheet.subsurface(rect))

        # Initialize animation variables
        self.direction = "down"
        self.image = self.animations[self.direction][0]
        self.rect = self.image.get_rect(center=position)
        self.frame_index = 0

    # Update the player's position and animation. This is used to move the player and animate the sprite based on input.
    def update(self, pressed_keys):
        # Movement variables
        move_x = 0
        move_y = 0

        # Update movement and direction
        if pressed_keys[pygame.K_UP]:
            move_y = -PLAYER_SPEED
            self.direction = "up"
        elif pressed_keys[pygame.K_DOWN]:
            move_y = PLAYER_SPEED
            self.direction = "down"
        if pressed_keys[pygame.K_LEFT]:
            move_x = -PLAYER_SPEED
            self.direction = "left"
        elif pressed_keys[pygame.K_RIGHT]:
            move_x = PLAYER_SPEED
            self.direction = "right"

        # Move the player
        self.rect.x += move_x
        self.rect.y += move_y

        # Animate if moving
        if move_x != 0 or move_y != 0:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.animations[self.direction]):
                self.frame_index = 0
            self.image = self.animations[self.direction][int(self.frame_index)]
        else:
            # Reset animation frame if not moving
            self.frame_index = 0
            self.image = self.animations[self.direction][int(self.frame_index)]

        # Keep the player within screen bounds
        self.rect.clamp_ip(SCREEN.get_rect())


# Create a player instance at the center of the screen
player = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
# Create a sprite group to manage rendering and updates
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Set up the game clock for frame rate management
clock = pygame.time.Clock()


# Create a menu instance
menu = menu.Menu(SCREEN)
menu.display_menu()

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current state of all keyboard buttons
    pressed_keys = pygame.key.get_pressed()
    # Update all sprites based on input
    all_sprites.update(pressed_keys)

    # Clear the screen with a background color
    SCREEN.fill((34, 139, 34))  # Forest green background

    # Draw all sprites onto the screen
    all_sprites.draw(SCREEN)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)
