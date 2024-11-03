import pygame
from pygame.math import Vector2
from constants import (
    PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_THRUST_POWER,
    PLAYER_FRICTION, SCREEN_WIDTH, SCREEN_HEIGHT,
    PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN
)
from circleshape import CircleShape
from shot import Shot  # Import the Shot class


class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)  # Call parent constructor with PLAYER_RADIUS
        self.rotation = 0  # Initialize rotation to 0 degrees
        self.velocity = Vector2(0, 0)  # Initialize velocity vector
        self.shoot_cooldown = 0  # Time until the player can shoot again


    def triangle(self):
        """Calculates the vertices of the triangle representing the player."""
        # Forward vector points upwards initially
        forward = Vector2(0, -1).rotate(self.rotation)
        # Right vector points to the right initially
        right = Vector2(1, 0).rotate(self.rotation) * self.radius / 1.5
        # Calculate the three points of the triangle
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def rotate_player(self, direction: float, dt: float):
        """Rotates the player by PLAYER_TURN_SPEED degrees per second."""
        self.rotation += PLAYER_TURN_SPEED * direction * dt
        self.rotation %= 360  # Ensure the rotation stays within 0-359 degrees


    def apply_thrust(self, thrust_power: float, dt: float):
        """
        Applies thrust to the player.
      
        :param thrust_power: Positive for forward thrust, negative for reverse thrust.
        :param dt: Delta time in seconds.
        """
        # Calculate the thrust vector based on current rotation
        thrust = Vector2(0, -thrust_power).rotate(self.rotation)
        # Update velocity
        self.velocity += thrust * dt


    def shoot(self):
        """Creates a new shot and sets its velocity based on the player's current direction."""
        # Create a new shot at the tip of the player's triangle
        forward = Vector2(0, -1).rotate(self.rotation)
        shot_position = self.position + forward * (self.radius + SHOT_RADIUS)
        shot = Shot(shot_position.x, shot_position.y)

        # Set the shot's velocity
        shot.velocity = forward * PLAYER_SHOOT_SPEED


    def update(self, dt: float):
        """Updates the player's state based on user input."""
        keys = pygame.key.get_pressed()


        # Rotation controls
        if keys[pygame.K_a]:
            self.rotate_player(-1, dt)  # Rotate left
        if keys[pygame.K_d]:
            self.rotate_player(1, dt)   # Rotate right


        # Thrust controls
        if keys[pygame.K_w]:
            self.apply_thrust(PLAYER_THRUST_POWER, dt)  # Forward thrust
        if keys[pygame.K_s]:
            self.apply_thrust(-PLAYER_THRUST_POWER, dt)  # Reverse thrust


        # Shooting controls
        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown <= 0:
                self.shoot()
                self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN  # Use the constant


        # Update shooting cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt
            if self.shoot_cooldown < 0:
                self.shoot_cooldown = 0  # Prevent negative cooldown


        # Update position based on velocity
        self.position += self.velocity * dt


        # Apply friction to simulate gradual slowing down
        self.velocity *= PLAYER_FRICTION


        # Screen wrapping
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0


        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0


    def draw(self, screen):
        """Draws the player as a triangle on the screen."""
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
