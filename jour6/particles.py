import pygame
import random

class Particle:
    def __init__(self, pos):
        self.pos = pygame.Vector2(pos)
        self.vel = pygame.Vector2(random.uniform(-2,2),
                                  random.uniform(-3,0))
        self.life = 30

    def update(self):
        self.pos += self.vel
        self.life -= 1

    def draw(self, screen):
        if self.life > 0:
            pygame.draw.circle(screen, (200,200,200),
                               (int(self.pos.x), int(self.pos.y)), 3)