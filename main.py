import pygame

from constants import *
from player import Player


def main():
    pygame.init()

    #set up the screen 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Instantiate the Player in the center of the screen
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
   
   #Initialize the clock and delta time
    clock = pygame.time.Clock()
    dt = 0

    # Game loop
    while True:

        #Event handling
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
                return

        # Fill screen with black color
        screen.fill("black") 

        #draw player
        player.draw(screen)

        #Updates the display
        pygame.display.flip()

        #Limit FPS to 60 and calculaet delta
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

