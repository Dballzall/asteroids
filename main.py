import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from highscore import load_high_score, save_high_score
import time  # Add this import


def show_game_over_screen(screen, score, high_score):
    """Display the game over screen with scores."""
    font_large = pygame.font.SysFont(None, 64)  # Larger font for "Game Over!"
    font_normal = pygame.font.SysFont(None, 32)  # Normal font for scores
    
    # Render the text
    game_over_text = font_large.render("Game Over!", True, "white")
    score_text = font_normal.render(f"Final Score: {score}", True, "white")
    high_score_text = font_normal.render(f"High Score: {high_score}", True, "yellow")
    
    # Get the text positions (centered on screen)
    game_over_pos = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50))
    score_pos = score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 10))
    high_score_pos = high_score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))
    
    # Clear screen and draw the text
    screen.fill("black")
    screen.blit(game_over_text, game_over_pos)
    screen.blit(score_text, score_pos)
    screen.blit(high_score_text, high_score_pos)
    pygame.display.flip()
    
    # Wait for 3 seconds
    time.sleep(3)

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
                    player.lives = 0  # Ensure lives don't go negative

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    score += 10  # Update the score
                    # Update high score if current score is higher
                    if score > high_score:
                        high_score = score
                        save_high_score(high_score)

        # Modify the game over condition
        if player.lives <= 0:
            if score > high_score:
                save_high_score(score)
            show_game_over_screen(screen, score, high_score)
            return

        screen.fill("black")

        # Render just the score and lives (removed high score)
        score_text = font.render(f"Score: {score}", True, "white")
        lives_text = font.render(f"Lives: {player.lives}", True, "white")
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 35))  # Moved up since we removed high score

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
