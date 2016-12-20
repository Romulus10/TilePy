import pygame

import TilePy


class Player(object):
    def __init__(self, sprite_list, x, y):
        self.sprite_list = sprite_list
        self.original_pos_x = x
        self.original_pos_y = y
        self.pos_x = x
        self.pos_y = y
        self.speed_x = 0
        self.speed_y = 0
        self.facing = "down"
        self.inventory = []

    def draw(self, screen, this_map):
        player = None
        self.check_pos()
        self.check_collision(this_map)
        if self.facing == "down":
            player = pygame.image.load("../" + self.sprite_list[0])
        if self.facing == "up":
            player = pygame.image.load("../" + self.sprite_list[1])
        if self.facing == "right":
            player = pygame.image.load("../" + self.sprite_list[2])
        if self.facing == "left":
            player = pygame.image.load("../" + self.sprite_list[3])
        screen.blit(player, [self.pos_x * 32, self.pos_y * 32])

    def move(self, direction):
        self.facing = direction
        if direction == "down":
            self.speed_y = 1
        if direction == "up":
            self.speed_y = -1
        if direction == "right":
            self.speed_x = 1
        if direction == "left":
            self.speed_x = -1

    def stop(self):
        self.speed_x = 0
        self.speed_y = 0

    def check_pos(self):
        self.pos_y += self.speed_y
        self.pos_x += self.speed_x

    def check_collision(self, this_map):
        # DONE Check collision with NPC.
        try:
            if this_map.tiles[self.pos_x][self.pos_y] in this_map.wall_values:
                if self.facing == "left":
                    self.stop()
                    self.pos_x += 1
                if self.facing == "right":
                    self.stop()
                    self.pos_x -= 1
                if self.facing == "up":
                    self.stop()
                    self.pos_y += 1
                if self.facing == "down":
                    self.stop()
                    self.pos_y -= 1
            for x in this_map.entities:
                if (self.pos_x == x.pos_x and self.pos_y == x.pos_y) and not x.done:
                    if self.facing == "left":
                        self.stop()
                        self.pos_x += 1
                    if self.facing == "right":
                        self.stop()
                        self.pos_x -= 1
                    if self.facing == "up":
                        self.stop()
                        self.pos_y += 1
                    if self.facing == "down":
                        self.stop()
                        self.pos_y -= 1
        except IndexError:
            TilePy.game.game_log("Outside the map. Repositioning.", 2)
            # HACK Addresses the Dancing Off the Map bug. Not very graceful - should be fixed ASAP.
            self.pos_x = self.original_pos_x
            self.pos_y = self.original_pos_y

    def check_for_interaction(self, this_map):
        # DONE Test check_for_interaction
        # DONE Rewrite check_for_interaction.
        for x in this_map.entities:
            if x.pos_x == self.pos_x - 1 and self.facing == "left":
                x.interact_with(self)
            if x.pos_x == self.pos_x + 1 and self.facing == "right":
                x.interact_with(self)
            if x.pos_y == self.pos_y - 1 and self.facing == "up":
                x.interact_with(self)
            if x.pos_y == self.pos_y + 1 and self.facing == "down":
                x.interact_with(self)

    def get_inventory(self):
        TilePy.game.game_log("Player inventory: " + str(self.inventory), 0)
