import pygame

from constants import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Game loop
    while True:

        #Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill screen with black color
        screen.fill((0,0,0)) # RGB for black

        #Updates the display
        pygame.display.flip()

if __name__ == "__main__":
    main()

