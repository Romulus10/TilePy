import pygame

# import pdb

import TilePy

game = TilePy.begin("Test")

game.maps = [
    TilePy.Map("test",
               [[1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1]],
               [1],
               ['assets/images/wood_floor.png', 'assets/images/wood_wall.png'],
               6,
               6,
               [TilePy.Item("rock", False, ['assets/images/test.png'], 2, 2, "I got a rock..."),
                TilePy.Actor("actor", False,
                             ["assets/images/arrow_down.png", "assets/images/arrow_up.png",
                              "assets/images/arrow_right.png", "assets/images/arrow_left.png"], 1, 1,
                             ["I am an NPC!", "Hello!"], "up", 10, 1, 1, False),
                TilePy.Actor("actor", False,
                             ["assets/images/arrow_down.png", "assets/images/arrow_up.png",
                              "assets/images/arrow_right.png", "assets/images/arrow_left.png"], 4, 4,
                             ["I am an enemy!", "Hello!"], "up", 10, 1, 1, True)
                ])
]

game.current_map = game.maps[0]

player = TilePy.Player(["assets/images/arrow_down.png", "assets/images/arrow_up.png", "assets/images/arrow_right.png",
                        "assets/images/arrow_left.png"], 3, 3, 10, 1, 1)

pygame.init()

screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()

game.ready()
done = False

test = []

while not done:

    # pdb.set_trace()

    screen.fill((0, 0, 0))

    game.current_map.draw(screen)

    player.draw(screen, game.current_map)

    for x in game.dialog_window_stack:
        x.draw(screen)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
            game.game_log("Quitting game_object.", 0)

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
            if event.key == pygame.K_t:
                player.check_for_attack(game.current_map)
            if event.key == pygame.K_x:
                if TilePy.check_for_open_window_and_close(game):
                    pass
                else:
                    player.check_for_interaction(game.current_map)
            game.game_log(game.dialog_window_stack, 1)

    pygame.display.flip()

    clock.tick(game.FPS)
