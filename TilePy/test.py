import pygame

import TilePy

current_map = TilePy.Map("test", [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
                         ['wood_wall.png'], 5, 5)

pygame.init()

screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()

done = False

while not done:
    screen.fill((0, 0, 0))

    current_map.draw(screen)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
            print("Quitting game.")

    pygame.display.flip()

    clock.tick(60)
