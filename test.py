import sys

import pygame

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
                             ["I am an NPC!", "Hello!"], "up", 20, 1, 1, False),
                TilePy.Actor("actor", False,
                             ["assets/images/arrow_down.png", "assets/images/arrow_up.png",
                              "assets/images/arrow_right.png", "assets/images/arrow_left.png"], 4, 4,
                             ["I am an enemy!", "Hello!"], "up", 20, 1, 1, True),
                ]),
    TilePy.Map("test2",
               [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
               [1],
               ['assets/images/wood_floor.png', 'assets/images/wood_wall.png'],
               10,
               10,
               [])
]

game.maps[0].entities.append(TilePy.MapGate(3, 1, game.maps[0], game.maps[1], "assets/images/door.png"))
game.maps[1].entities.append(TilePy.MapGate(3, 1, game.maps[1], game.maps[0], "assets/images/door.png"))

player = TilePy.Player(["assets/images/arrow_down.png", "assets/images/arrow_up.png", "assets/images/arrow_right.png",
                        "assets/images/arrow_left.png"], 3, 3, 20, 1, 1, game.maps[0])

menus = [TilePy.Menu(["Test", "This", "Menu"])]

pygame.init()

screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()

game.ready()
done = False

test = []

while not done:

    # pdb.set_trace()

    screen.fill((0, 0, 0))

    player.map.draw(screen)

    player.draw(screen)

    for x in game.dialog_window_stack:
        x.draw(screen)

    for x in menus:
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
                if not TilePy.menu_move_down(menus):
                    player.move("down")
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if not TilePy.menu_move_up(menus):
                    player.move("up")
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.move("right")
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.move("left")
            if event.key == pygame.K_i:
                player.get_inventory()
            if event.key == pygame.K_t:
                player.check_for_attack()
            if event.key == pygame.K_f:
                if TilePy.check_for_open_menu_and_close(menus):
                    pass
                else:
                    menus[0].show()
            if event.key == pygame.K_x:
                if TilePy.check_for_open_window_and_close(game):
                    pass
                else:
                    player.check_for_interaction()
            game.game_log(game.dialog_window_stack, 1)

    if player.check_death():
        # TODO Please don't leave this this way.
        print("You have died.")
        pygame.quit()
        sys.exit()

    pygame.display.flip()

    clock.tick(game.FPS)
