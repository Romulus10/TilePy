import pygame

import TilePy

game = TilePy.Game()

current_map = TilePy.Map("test",
                         [[0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0]],
                         [1],
                         ['wood_floor.png', 'wood_wall.png'],
                         5,
                         5,
                         [TilePy.NPC("rock", "item", False, ['test.png'])],
                         [[0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 1, 0, 0, 0],
                          [0, 0, 0, 0, 0]])

player = TilePy.Player(["trainer_down.png", "trainer_up.png", "trainer_right.png", "trainer_left.png"], 0, 0)

pygame.init()

screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()

done = False

while not done:
    screen.fill((0, 0, 0))

    current_map.draw(screen)

    player.draw(screen, current_map)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
            print("Quitting game.")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.stop()
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.stop()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.stop()
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.stop()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.move("down")
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.move("up")
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.move("right")
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.move("left")
            if event.key == pygame.K_a:
                player.check_for_interaction(current_map)

    pygame.display.flip()

    clock.tick(game.FPS)
