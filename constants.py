SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
PLAYER_RADIUS = 20  # Adjust as needed
PLAYER_TURN_SPEED = 300  # Degrees per second
PLAYER_THRUST_POWER = 300  # Pixels per second squared
PLAYER_FRICTION = 0.99  # Friction coefficient (between 0 and 1)

# Add these new constants
SCORE_THRESHOLD = 100  # Points needed for each speed increase
ASTEROID_SPEED_INCREASE = 1.2  # Speed multiplier for each threshold reached

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

SHOT_RADIUS = 5
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.25