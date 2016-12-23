import pygame

import TilePy
import tools


class Player(object):
    def __init__(self, sprite_list, x, y, health, attack, defense):
        self.sprite_list = sprite_list
        self.original_pos_x = x
        self.original_pos_y = y
        self.pos_x = x
        self.pos_y = y
        self.speed_x = 0
        self.speed_y = 0
        self.facing = "down"
        self.inventory = []
        self.health = health
        self.attack = attack
        self.defense = defense

    def draw(self, screen, this_map):
        """
        :param screen: A pygame.Surface object
        :param this_map: The TilePy.Map object to be drawn
        """
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
        """
        :param direction: Initial direction - "up", "down", "left", or "right"
        """
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
        """
        :param this_map: A TilePy.Map object
        """
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
            TilePy.game_object.game_log("Outside the map. Repositioning.", 2)
            # HACK Addresses the Dancing Off the Map bug. Not very graceful - should be fixed ASAP.
            self.pos_x = self.original_pos_x
            self.pos_y = self.original_pos_y

    def check_for_interaction(self, this_map):
        for x in this_map.entities:
            if x.pos_x == self.pos_x - 1 and self.facing == "left":
                x.interact_with(self)
            if x.pos_x == self.pos_x + 1 and self.facing == "right":
                x.interact_with(self)
            if x.pos_y == self.pos_y - 1 and self.facing == "up":
                x.interact_with(self)
            if x.pos_y == self.pos_y + 1 and self.facing == "down":
                x.interact_with(self)

    def check_for_attack(self, this_map):
        for x in this_map.entities:
            if x.pos_x == self.pos_x - 1 and self.facing == "left":
                self.try_attack(x)
            if x.pos_x == self.pos_x + 1 and self.facing == "right":
                self.try_attack(x)
            if x.pos_y == self.pos_y - 1 and self.facing == "up":
                self.try_attack(x)
            if x.pos_y == self.pos_y + 1 and self.facing == "down":
                self.try_attack(x)

    def get_inventory(self):
        TilePy.game_object.game_log("Player inventory: " + str(self.inventory), 0)

    def try_attack(self, target):
        print("Target Health: " + str(target.health))
        if target.is_attackable:
            target.health -= tools.calculate_damage(self.attack, target.defense)
            print("Updated Target Health: " + str(target.health))
            target.check_if_dead()
        else:
            print("Target is not a valid target.")
            pass
