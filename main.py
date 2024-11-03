import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids!")

    # Instantiate the Player in the center of the screen
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
   
    # Initialize the clock and delta time
    clock = pygame.time.Clock()
    dt = 0

    # Game loop
    running = True
    while running:

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the game loop

        # Handle player updates
        player.update(dt)
       
        # Fill screen with black color using RGB tuple
        screen.fill((0, 0, 0)) 

        # Draw player
        player.draw(screen)

        # Update the display
        pygame.display.flip()

        # Limit FPS to 60 and calculate delta time
        dt = clock.tick(60) / 1000  # Delta time in seconds

    # Properly quit Pygame after exiting the loop
    pygame.quit()

if __name__ == "__main__":
    main()
