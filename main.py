import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from highscore import load_high_score, save_high_score


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids!")
    clock = pygame.time.Clock()
    
    # Initialize Font
    pygame.font.init()
    font = pygame.font.SysFont(None, 24)  # Adjusted font size to 24 for smaller text

    # Initialize Score and High Score
    score = 0
    high_score = load_high_score()  # Load the high score

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Save high score before quitting
                if score > high_score:
                    save_high_score(score)
                return

        # Update asteroid field's current score
        asteroid_field.current_score = score

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player) and not player.invulnerable:
                player.lives -= 1
                if player.lives > 0:
                    # Respawn player
                    player.reset_position()
                else:
                    print("Game over!")
                    if score > high_score:
                        save_high_score(score)
                    return

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    score += 10  # Update the score
                    # Update high score if current score is higher
                    if score > high_score:
                        high_score = score
                        save_high_score(high_score)

        screen.fill("black")

        # Render the score and high score
        score_text = font.render(f"Score: {score}", True, "white")
        high_score_text = font.render(f"High Score: {high_score}", True, "yellow")
        lives_text = font.render(f"Lives: {player.lives}", True, "white")
        screen.blit(score_text, (10, 10))
        screen.blit(high_score_text, (10, 35))
        screen.blit(lives_text, (10, 60))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
