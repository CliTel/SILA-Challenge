import pygame
from settings import TILE_SIZE

def create_grass_tile():
    surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
    surface.fill((139, 69, 19))
    pygame.draw.rect(surface, (34, 177, 76),
                     (0, 0, TILE_SIZE, TILE_SIZE // 4))
    return surface

def create_stone_tile():
    surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
    surface.fill((100, 100, 100))
    pygame.draw.rect(surface, (50,50,50), (0,0,TILE_SIZE,TILE_SIZE))
    return surface

def generate_tileset():
    return {
        1: create_grass_tile(),
        2: create_stone_tile()
    }