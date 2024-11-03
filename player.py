import pygame
from pygame.math import Vector2
from constants import PLAYER_RADIUS
from circleshape import CircleShape  # Adjust the import based on your project structure

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)  # Call parent constructor with PLAYER_RADIUS
        self.rotation = 0  # Initialize rotation to 0

    def triangle(self):
        forward = Vector2(0, -1).rotate(self.rotation)
        right = Vector2(1, 0).rotate(self.rotation) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
