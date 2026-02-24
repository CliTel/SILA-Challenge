import pygame
from settings import PROJECTILE_SPEED

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((10,5))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect(center=(x,y))
        self.vel = pygame.Vector2(direction * PROJECTILE_SPEED, 0)

    def update(self):
        self.rect.x += self.vel.x
        if self.rect.right < 0 or self.rect.left > 1000:
            self.kill()