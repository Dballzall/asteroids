import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids!")
    clock = pygame.time.Clock()

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()  # Group for shots

    # Assign containers to classes
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)  # Shots are updatable and drawable
    Player.containers = (updatable, drawable)

    # Initialize game objects
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update all updatable objects
        updatable.update(dt)

        # Check for collisions between asteroids and player
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                pygame.quit()
                sys.exit()

        #Collision Detection: Asteroids vs. Shots
        for asteroid in asteroids.copy():
            for shot in shots.copy():
                if asteroid.collides_with(shot):
                    asteroid.kill()  # Remove asteroid
                    shot.kill()      # Remove shot
                    break  # Move to the next asteroid after collision

        # Draw everything
        screen.fill("black")

        # Use custom draw methods by iterating through drawable
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # Limit the framerate to 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
