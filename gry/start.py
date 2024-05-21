# https://www.renpy.org/ - biblioteka do tworzenia gier (novelek wizualnych)
# 
# PyGame wprowadzenie
# https://realpython.com/pygame-a-primer/
#
# do Tworzenia aplikacji https://kivy.org/

# Simple pygame program

# Import and initialize the pygame library
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)



# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 0, 255))   #różowy
        self.rect = self.surf.get_rect()
    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

#Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Run until the user asks to quit
running = True
y = 0




while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    

    # Draw a solid blue circle in the center
    #pygame.draw.circle(screen, (255, 0, 0), (250,y), 70)

    # Create a surface and pass in a tuple containing its length and width
    #surf = pygame.Surface((50, 50))

    #surf.fill((0, 0, 0))
    #rect = surf.get_rect()
    
    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Fill the background with black
    screen.fill((0,0,0))
    #narysuj gracza po środku ekranu
    screen.blit(player.surf, player.rect)
    
    
    
    # This line says "Draw surf onto the screen at the center"
    #screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()