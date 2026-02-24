import pygame
from settings import *
from physics import apply_gravity, apply_friction
from collision import collide_aabb
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30,40))
        self.image.fill((0,200,255))
        self.rect = self.image.get_rect(topleft=(x,y))
        self.mask = pygame.mask.from_surface(self.image)
        self.vel = pygame.Vector2(0,0)
        self.on_ground = False
        self.score = 0
        self.lives = PLAYER_LIVES
        self.projectiles = pygame.sprite.Group()

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vel.x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.vel.x = PLAYER_SPEED
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel.y = JUMP_POWER
        if keys[pygame.K_f]:
            direction = 1 if keys[pygame.K_RIGHT] else -1
            self.projectiles.add(Projectile(self.rect.centerx,
                                            self.rect.centery,
                                            direction))

    def update(self, tiles):
        self.input()
        apply_gravity(self)
        apply_friction(self)

        self.rect.x += self.vel.x
        for tile in collide_aabb(self, tiles):
            if self.vel.x > 0:
                self.rect.right = tile.rect.left
            if self.vel.x < 0:
                self.rect.left = tile.rect.right

        self.rect.y += self.vel.y
        self.on_ground = False
        for tile in collide_aabb(self, tiles):
            if self.vel.y > 0:
                self.rect.bottom = tile.rect.top
                self.vel.y = 0
                self.on_ground = True
            if self.vel.y < 0:
                self.rect.top = tile.rect.bottom
                self.vel.y *= BOUNCE

        self.projectiles.update()