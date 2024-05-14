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

pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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

    # Fill the background with white
    screen.fill((255,255,255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (255, 0, 0), (250,y), 70)
    
    # Create a surface and pass in a tuple containing its length and width
    surf = pygame.Surface((50, 50))

    surf.fill((0, 0, 0))
    rect = surf.get_rect()
    
    # This line says "Draw surf onto the screen at the center"
    screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()