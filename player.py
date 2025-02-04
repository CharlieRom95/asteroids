import sys
print(sys.path)

from circleshape import CircleShape
from constants import *
import pygame 
from shot import Shot




class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.PLAYER_SHOOT_COOLDOWN = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):

        self.PLAYER_SHOOT_COOLDOWN -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.movef(dt)

        if keys[pygame.K_s]:
            self.moveb(dt)

        if keys[pygame.K_SPACE]:
            if self.PLAYER_SHOOT_COOLDOWN <= 0:
                self.shoot()
                self.PLAYER_SHOOT_COOLDOWN = 0.3

    def movef(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def moveb(self, dt):
        backward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += backward * PLAYER_SPEED * dt

    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y)
        bullet = pygame.Vector2(0, 1).rotate(self.rotation)
        new_shot.velocity = bullet*PLAYER_SHOOT_SPEED
        
        
