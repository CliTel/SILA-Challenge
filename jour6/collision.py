import pygame

def collide_aabb(sprite, tiles):
    collisions = []
    for tile in tiles:
        if sprite.rect.colliderect(tile.rect):
            collisions.append(tile)
    return collisions

def collide_mask(sprite1, sprite2):
    return pygame.sprite.collide_mask(sprite1, sprite2)