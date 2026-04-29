from circleshape import CircleShape # pyright: ignore[reportMissingImports]
import pygame # pyright: ignore[reportMissingImports]
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot #pyright: ignore[reportMissingImports]

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.cooldown > 0:
            return
        else:
            self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def update(self, dt):
        self.cooldown = self.cooldown - dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-1)
        if keys[pygame.K_d]:
            self.rotate(1)
        if keys[pygame.K_w]:
            self.move(1)
        if keys[pygame.K_s]:
            self.move(-1)
        if keys[pygame.K_SPACE]:
            self.shoot()
