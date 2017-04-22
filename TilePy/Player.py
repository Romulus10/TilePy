import pygame

import MapGate
import TilePy
import tools


class Player(object):
    def __init__(self, sprite_list, x, y, health, attack, defense, this_map):
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
        self.map = this_map

    def draw(self, screen):
        """
        :param screen: A pygame.Surface object
        """
        player = None
        self.check_pos()
        self.check_collision()
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

    def check_collision(self):
        try:
            if self.map.tiles[self.pos_x][self.pos_y] in self.map.wall_values:
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
            for x in self.map.entities:
                if (self.pos_x == x.pos_x and self.pos_y == x.pos_y) and not x.done \
                        and not isinstance(x, MapGate.MapGate):
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
                if isinstance(x, MapGate.MapGate) and (self.pos_x == x.pos_x and self.pos_y == x.pos_y):
                    self.pos_x = x.pos_x
                    self.pos_y = x.pos_y + 1
                    self.map = x.to_map
        except IndexError:
            TilePy.game_object.game_log("Outside the map. Repositioning.", 2)
            # HACK Addresses the Dancing Off the Map bug. Not very graceful - should be fixed ASAP.
            self.pos_x = self.original_pos_x
            self.pos_y = self.original_pos_y

    def check_for_interaction(self):
        for x in self.map.entities:
            if x.pos_x == self.pos_x - 1 and x.pos_y == self.pos_y and self.facing == "left":
                x.interact_with(self)
            if x.pos_x == self.pos_x + 1 and x.pos_y == self.pos_y and self.facing == "right":
                x.interact_with(self)
            if x.pos_y == self.pos_y - 1 and x.pos_x == self.pos_x and self.facing == "up":
                x.interact_with(self)
            if x.pos_y == self.pos_y + 1 and x.pos_x == self.pos_x and self.facing == "down":
                x.interact_with(self)

    def check_for_attack(self):
        for x in self.map.entities:
            if x.pos_x == self.pos_x - 1 and x.pos_y == self.pos_y and self.facing == "left":
                self.try_attack(x)
            if x.pos_x == self.pos_x + 1 and x.pos_y == self.pos_y and self.facing == "right":
                self.try_attack(x)
            if x.pos_y == self.pos_y - 1 and x.pos_x == self.pos_x and self.facing == "up":
                self.try_attack(x)
            if x.pos_y == self.pos_y + 1 and x.pos_x == self.pos_x and self.facing == "down":
                self.try_attack(x)

    def get_inventory(self):
        TilePy.game_object.game_log("Player inventory: " + str(self.inventory), 0)

    def try_attack(self, target):
        if target.is_attackable:
            print("Target Health: " + str(target.health))
            target.health -= tools.calculate_damage(self.attack, target.defense)
            print("Updated Target Health: " + str(target.health))
            if not target.check_if_dead():
                print("Player Health: " + str(self.health))
                self.health -= tools.calculate_damage(target.attack, self.defense)
                print("Updated Player Health: " + str(self.health))
        else:
            print("Target is not a valid target.")

    def check_death(self):
        if self.health <= 0:
            return True
        else:
            return False
