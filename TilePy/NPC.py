import pygame

import TilePy
from DialogWindow import DialogWindow


class NPC(object):
    # TODO NPC AI Movement
    # TODO Determine what dialog box to display when self.done
    def __init__(self, name, done, sprite_list, x, y, attackable):
        self.name = name
        self.done = done
        self.sprite_list = sprite_list
        self.pos_x = x
        self.pos_y = y
        self.visible = True
        self.is_attackable = attackable

    def interact_with(self, player):
        # TODO NPC Interactions
        TilePy.game_object.game_log("interacting with " + self.name, 0)

    def draw(self, screen):
        # TODO Handle moving NPCs.
        # TODO Handle differentiating between items and people and projectiles.
        if self.visible:
            player = pygame.image.load(self.sprite_list[0])
            screen.blit(player, [self.pos_x * 32, self.pos_y * 32])


class Actor(NPC):
    """
    Implements a human-type NPC that the player can talk to.
    """

    def __init__(self, name, done, sprite_list, x, y, text, facing, health, attack, defense, attackable):
        """
        :param name: The name of the actor
        :param done: Whether we've talked to them already or not
        :param sprite_list: Images used for this actor.
        :param x: Initial x position.
        :param y: Initial y position.
        :param text: Any dialog windows to be displayed. These should be in the list in REVERSE ORDER.
        :param facing: Initial direction - "up", "down", "left", or "right"
        """
        super(Actor, self).__init__(name, done, sprite_list, x, y, attackable)
        self.text = text
        self.facing = facing
        self.health = health
        self.attack = attack
        self.defense = defense

    def draw(self, screen):
        if self.visible:
            player = pygame.image.load(self.sprite_list[0])
            if self.facing == "down":
                player = pygame.image.load(self.sprite_list[0])
            if self.facing == "up":
                player = pygame.image.load(self.sprite_list[1])
            if self.facing == "right":
                player = pygame.image.load(self.sprite_list[2])
            if self.facing == "left":
                player = pygame.image.load(self.sprite_list[3])
            screen.blit(player, [self.pos_x * 32, self.pos_y * 32])

    def turn_to_face_player(self, player):
        if player.pos_x == self.pos_x - 1:
            self.facing = "left"
        elif player.pos_x == self.pos_x + 1:
            self.facing = "right"
        elif player.pos_y == self.pos_y + 1:
            self.facing = "down"
        elif self.pos_y == self.pos_y - 1:
            self.facing = "up"

    def interact_with(self, player):
        if not self.done:
            self.turn_to_face_player(player)
            for x in self.text:
                var = DialogWindow(x)
                var.show()
                TilePy.game_object.dialog_window_stack.append(var)

    def check_if_dead(self):
        if self.health <= 0:
            self.visible = False
            self.done = True


class ShopKeep(NPC):
    """
    Implements an NPC entity with an inventory that the player can trade with.
    """

    def __init__(self, name, done, sprite_list, x, y, ):
        super(ShopKeep, self).__init__(name, done, sprite_list, x, y, False)


class Item(NPC):
    """
    To add items to a game_object using the TilePy library, they should be new classes that extend the Item class.
    They should however ONLY override the "use" method. All other methods should work fine.
    """

    def __init__(self, name, done, sprite_list, x, y, msg, ):
        super(Item, self).__init__(name, done, sprite_list, x, y, False)
        self.text = msg
        self.in_inventory = False

    def interact_with(self, player):
        if not self.done:
            TilePy.game_object.game_log(TilePy.game_object.dialog_window_stack, 1)
            TilePy.game_object.game_log("added to inventory: " + self.name, 0)
            var = DialogWindow(self.text)
            var.show()
            TilePy.game_object.dialog_window_stack.append(var)
            self.done = True
            self.in_inventory = True
            player.inventory.append(self)

    def draw(self, screen):
        """
        :param screen: a pygame.Surface object.
        """
        if not self.done:
            player = pygame.image.load(self.sprite_list[0])
            screen.blit(player, [self.pos_x * 32, self.pos_y * 32])

    def use(self):
        """
        This is a stub to be inherited by game_object-specific Item objects.
        """
        # TODO Implement using items in inventory.
        if self.in_inventory:
            TilePy.game_object.game_log("Using " + self.name, 0)
        else:
            TilePy.game_object.game_log("Item not in player inventory " + self.name, 0)
