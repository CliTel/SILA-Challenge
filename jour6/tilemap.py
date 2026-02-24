import pygame
import json
from settings import TILE_SIZE
from tileset import generate_tileset

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

def load_level(path):
    tiles = []
    tileset = generate_tileset()

    with open(path) as f:
        data = json.load(f)

    for row_index, row in enumerate(data["tiles"]):
        for col_index, tile_id in enumerate(row):
            if tile_id in tileset:
                tiles.append(Tile(col_index*TILE_SIZE,
                                  row_index*TILE_SIZE,
                                  tileset[tile_id]))
    return tiles