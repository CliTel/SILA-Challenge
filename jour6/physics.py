from settings import GRAVITY, FRICTION

def apply_gravity(entity):
    entity.vel.y += GRAVITY

def apply_friction(entity):
    entity.vel.x += entity.vel.x * FRICTION