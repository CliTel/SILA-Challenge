import pygame
from settings import *
from player import Player
from enemy import Enemy
from tilemap import load_level
from collision import collide_mask
from ui import draw_text, save_highscore, load_highscore

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

current_level = 1
tiles = load_level(f"levels/level{current_level}.json")
player = Player(100, 100)
enemies = pygame.sprite.Group()
enemies.add(Enemy(700, 100))
highscore = load_highscore()

camera_x = 0
camera_y = 0

running = True
game_over = False

while running:
    clock.tick(FPS)
    screen.fill((30,30,50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        player.update(tiles)
        for enemy in enemies:
            enemy.update(tiles, player)

        # Projectiles -> détruire ennemis
        for projectile in player.projectiles:
            for enemy in enemies:
                if collide_mask(projectile, enemy):
                    projectile.kill()
                    enemy.kill()
                    player.score += 100

        # Collision joueur -> Game over
        for enemy in enemies:
            if collide_mask(player, enemy):
                player.lives -= 1
                if player.lives <= 0:
                    game_over = True
                else:
                    player.rect.topleft = (100,100)

        # Camera centrée
        camera_x = player.rect.centerx - WIDTH//2
        camera_y = player.rect.centery - HEIGHT//2

        # Affichage tiles
        for tile in tiles:
            screen.blit(tile.image,(tile.rect.x - camera_x,tile.rect.y - camera_y))
        screen.blit(player.image,(player.rect.x - camera_x,player.rect.y - camera_y))
        for enemy in enemies:
            screen.blit(enemy.image,(enemy.rect.x - camera_x,enemy.rect.y - camera_y))
        for projectile in player.projectiles:
            screen.blit(projectile.image,(projectile.rect.x - camera_x,projectile.rect.y - camera_y))

        draw_text(screen,f"Score: {player.score}",30,20,20)
        draw_text(screen,f"Lives: {player.lives}",30,20,50)
        draw_text(screen,f"Highscore: {highscore}",30,WIDTH-200,20)

        # Passage niveau
        if player.rect.right - camera_x > WIDTH:
            current_level += 1
            if current_level > 5:
                game_over = True
            else:
                tiles = load_level(f"levels/level{current_level}.json")
                player.rect.topleft = (100,100)
                enemies.empty()
                enemies.add(Enemy(700,100))

    else:
        draw_text(screen,"GAME OVER",60,WIDTH//2-150,HEIGHT//2-50)
        draw_text(screen,f"High Score: {highscore}",40,WIDTH//2-150,HEIGHT//2+20)

    pygame.display.flip()
pygame.quit()