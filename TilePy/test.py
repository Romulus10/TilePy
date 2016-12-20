import pygame

# import pdb

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
                         [TilePy.Item("rock", False, ['test.png'], 2, 2, "I got a rock...")])

player = TilePy.Player(["arrow_down.png", "arrow_up.png", "arrow_right.png", "arrow_left.png"], 3, 3)

pygame.init()

screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()

game.ready()
done = False

test = []

while not done:

    # pdb.set_trace()

    screen.fill((0, 0, 0))

    current_map.draw(screen)

    player.draw(screen, current_map)

    for x in game.dialog_window_stack:
        x.draw(screen)

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
            if event.key == pygame.K_i:
                player.get_inventory()
            if event.key == pygame.K_x:
                if TilePy.check_for_open_window_and_close(game):
                    pass
                else:
                    player.check_for_interaction(current_map)
            game.game_log(game.dialog_window_stack, 1)

    pygame.display.flip()

    clock.tick(game.FPS)
