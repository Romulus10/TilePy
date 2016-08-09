import pygame

import TilePy

game = TilePy.begin("Test")

current_map = TilePy.Map("test",
                         [[1, 1, 1, 1, 1],
                          [1, 0, 0, 0, 1],
                          [1, 0, 0, 0, 1],
                          [1, 0, 0, 0, 1],
                          [1, 1, 1, 1, 1]],
                         [1],
                         ['wood_floor.png', 'wood_wall.png'],
                         5,
                         5,
                         [TilePy.NPC("rock", False, ['test.png'], 2, 2)])

player = TilePy.Player(["trainer_down.png", "trainer_up.png", "trainer_right.png", "trainer_left.png"], 3, 3)

pygame.init()

screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()

game.ready()
done = False

while not done:
    screen.fill((0, 0, 0))

    current_map.draw(screen)

    player.draw(screen, current_map)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
            game.game_log("Quitting game.", 0)

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
            if event.key == pygame.K_x:
                player.check_for_interaction(current_map)

    pygame.display.flip()

    clock.tick(game.FPS)
