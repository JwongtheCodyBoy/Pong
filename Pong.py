import pygame, sys, random

pygame.init()

WIDTH, HEIGHT = 1280, 720
 
FONT = pg.font.Font("Satoshi-Variable.ttf", int(WIDTH/20))

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
CLOCK = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    CLOCK.tick(300)

