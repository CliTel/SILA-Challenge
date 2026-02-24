import pygame
from settings import *
from physics import apply_gravity
from collision import collide_aabb

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30,40))
        self.image.fill((255,50,50))
        self.rect = self.image.get_rect(topleft=(x,y))
        self.mask = pygame.mask.from_surface(self.image)
        self.vel = pygame.Vector2(ENEMY_SPEED,0)
        self.direction = 1

    def update(self, tiles, player):
        apply_gravity(self)
        # Poursuite si proche joueur
        if abs(player.rect.centerx - self.rect.centerx) < 200:
            self.direction = 1 if player.rect.centerx > self.rect.centerx else -1

        self.vel.x = ENEMY_SPEED * self.direction
        self.rect.x += self.vel.x
        for tile in collide_aabb(self, tiles):
            self.direction *= -1

        self.rect.y += self.vel.y
        for tile in collide_aabb(self, tiles):
            if self.vel.y > 0:
                self.rect.bottom = tile.rect.top
                self.vel.y = 0