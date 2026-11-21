import pygame
import random
import sys

pygame.init()

WIDTH = 600
HEIGHT = 750

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RACING GAME")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (25, 25, 25)
GREEN = (35, 130, 55)
GRAY = (65, 65, 65)
RED = (220, 30, 30)

font = pygame.font.SysFont("Arial", 35)

player = pygame.Rect(275, 600, 50, 90)

enemies = []
score = 0
speed = 6
game_over = False

road_lines = [i for i in range(0, HEIGHT, 150)]

running = True

while running:

    screen.fill(GREEN)

    pygame.draw.rect(screen, GRAY, (100, 0, 400, HEIGHT))

    for y in road_lines:
        pygame.draw.rect(screen, WHITE, (295, y, 10, 75))
        y += speed

    road_lines = [(y + speed) % HEIGHT for y in road_lines]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.left > 110:
            player.x -= 7

        if keys[pygame.K_RIGHT] and player.right < 490:
            player.x += 7

        if random.randint(1, 35) == 1:
            enemies.append(pygame.Rect(
                random.choice([145, 245, 345, 445]),
                -100, 50, 90
            ))

        for enemy in enemies[:]:
            enemy.y += speed

            if enemy.y > HEIGHT:
                enemies.remove(enemy)
                score += 1

            if player.colliderect(enemy):
                game_over = True

        speed = min(6 + score // 5, 14)

    pygame.draw.rect(screen, RED, player, border_radius=8)

    for enemy in enemies:
        pygame.draw.rect(screen, (30, 100, 230), enemy, border_radius=8)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (15, 15))

    if game_over:
        text = font.render("GAME OVER", True, RED)
        screen.blit(text, (190, 330))

        restart = font.render("Press R to restart", True, WHITE)
        screen.blit(restart, (150, 390))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            player.x = 275
            enemies.clear()
            score = 0
            speed = 6
            game_over = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()


import pygame
import random
import sys

pygame.init()

WIDTH = 600
HEIGHT = 750

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RACING GAME")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (25, 25, 25)
GREEN = (35, 130, 55)
GRAY = (65, 65, 65)
RED = (220, 30, 30)

font = pygame.font.SysFont("Arial", 35)

player = pygame.Rect(275, 600, 50, 90)

enemies = []
score = 0
speed = 6
game_over = False

road_lines = [i for i in range(0, HEIGHT, 150)]

running = True

while running:

    screen.fill(GREEN)

    pygame.draw.rect(screen, GRAY, (100, 0, 400, HEIGHT))

    for y in road_lines:
        pygame.draw.rect(screen, WHITE, (295, y, 10, 75))
        y += speed

    road_lines = [(y + speed) % HEIGHT for y in road_lines]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.left > 110:
            player.x -= 7

        if keys[pygame.K_RIGHT] and player.right < 490:
            player.x += 7

        if random.randint(1, 35) == 1:
            enemies.append(pygame.Rect(
                random.choice([145, 245, 345, 445]),
                -100, 50, 90
            ))

        for enemy in enemies[:]:
            enemy.y += speed

            if enemy.y > HEIGHT:
                enemies.remove(enemy)
                score += 1

            if player.colliderect(enemy):
                game_over = True

        speed = min(6 + score // 5, 14)

    pygame.draw.rect(screen, RED, player, border_radius=8)

    for enemy in enemies:
        pygame.draw.rect(screen, (30, 100, 230), enemy, border_radius=8)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (15, 15))

    if game_over:
        text = font.render("GAME OVER", True, RED)
        screen.blit(text, (190, 330))

        restart = font.render("Press R to restart", True, WHITE)
        screen.blit(restart, (150, 390))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            player.x = 275
            enemies.clear()
            score = 0
            speed = 6
            game_over = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()


import pygame
import random
import sys

pygame.init()

WIDTH = 600
HEIGHT = 750

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RACING GAME")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (25, 25, 25)
GREEN = (35, 130, 55)
GRAY = (65, 65, 65)
RED = (220, 30, 30)

font = pygame.font.SysFont("Arial", 35)

player = pygame.Rect(275, 600, 50, 90)

enemies = []
score = 0
speed = 6
game_over = False

road_lines = [i for i in range(0, HEIGHT, 150)]

running = True

while running:

    screen.fill(GREEN)

    pygame.draw.rect(screen, GRAY, (100, 0, 400, HEIGHT))

    for y in road_lines:
        pygame.draw.rect(screen, WHITE, (295, y, 10, 75))
        y += speed

    road_lines = [(y + speed) % HEIGHT for y in road_lines]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.left > 110:
            player.x -= 7

        if keys[pygame.K_RIGHT] and player.right < 490:
            player.x += 7

        if random.randint(1, 35) == 1:
            enemies.append(pygame.Rect(
                random.choice([145, 245, 345, 445]),
                -100, 50, 90
            ))

        for enemy in enemies[:]:
            enemy.y += speed

            if enemy.y > HEIGHT:
                enemies.remove(enemy)
                score += 1

            if player.colliderect(enemy):
                game_over = True

        speed = min(6 + score // 5, 14)

    pygame.draw.rect(screen, RED, player, border_radius=8)

    for enemy in enemies:
        pygame.draw.rect(screen, (30, 100, 230), enemy, border_radius=8)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (15, 15))

    if game_over:
        text = font.render("GAME OVER", True, RED)
        screen.blit(text, (190, 330))

        restart = font.render("Press R to restart", True, WHITE)
        screen.blit(restart, (150, 390))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            player.x = 275
            enemies.clear()
            score = 0
            speed = 6
            game_over = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
