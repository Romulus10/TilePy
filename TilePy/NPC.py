import pygame

from TilePy.DialogWindow import DialogWindow


class NPC(object):
    # TODO NPC AI Movement
    # TODO Determine what dialog box to display when self.done
    def __init__(self, name, done, sprite_list, x, y):
        self.name = name
        self.done = done
        self.sprite_list = sprite_list
        self.pos_x = x
        self.pos_y = y

    def interact_with(self, player):
        # DONE How do I get dialog to work with NPCs?
        # TODO NPC Interactions
        globals()['game'].game_log("interacting with " + self.name, 0)

    def draw(self, screen):
        # TODO Handle moving NPCs.
        # DONE Handle turning to face player.
        # TODO Handle differentiating between items and people and projectiles.
        # DONE Handle changing active sprite.
        player = pygame.image.load(self.sprite_list[0])
        screen.blit(player, [self.pos_x * 32, self.pos_y * 32])

    def path_act(self, direction):
        if direction is "up":
            self.pos_y += 1
        if direction is "down":
            self.pos_y -= 1
        if direction is "right":
            self.pos_x += 1
        if direction is "left":
            self.pos_x -= 1


class Actor(NPC):
    """
    Implements a human-type NPC that the player can talk to.
    """

    def __init__(self, name, done, sprite_list, x, y, text, facing):
        super(Actor, self).__init__(name, done, sprite_list, x, y)
        self.text = text
        self.facing = facing

    def draw(self, screen):
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
        self.turn_to_face_player(player)
        for x in self.text:
            var = DialogWindow(x)
            var.show()
            globals()['game'].dialog_window_stack.append(var)


class ShopKeep(NPC):
    """
    Implements an NPC entity with an inventory that the player can trade with.
    """

    def __init__(self, name, done, sprite_list, x, y):
        super(ShopKeep, self).__init__(name, done, sprite_list, x, y)


class Item(NPC):
    """
    To add items to a game using the TilePy library, they should be new classes that extend the Item class.
    They should however ONLY override the "use" method. All other methods should work fine.
    """

    # DONE Add using
    # DONE and picking up items.
    def __init__(self, name, done, sprite_list, x, y, msg):
        super(Item, self).__init__(name, done, sprite_list, x, y)
        self.text = msg
        self.in_inventory = False

    def interact_with(self, player):
        globals()['game'].game_log(globals()['game'].dialog_window_stack, 1)
        globals()['game'].game_log("added to inventory: " + self.name, 0)
        var = DialogWindow(self.text)
        var.show()
        globals()['game'].dialog_window_stack.append(var)
        self.done = True
        self.in_inventory = True
        player.inventory.append(self)

    def draw(self, screen):
        if not self.done:
            player = pygame.image.load(self.sprite_list[0])
            screen.blit(player, [self.pos_x * 32, self.pos_y * 32])

    def use(self):
        """
        This is a stub to be inherited by game-specific Item objects.
        :return:
        """
        if self.in_inventory:
            globals()['game'].game_log("Using " + self.name, 0)
        else:
            globals()['game'].game_log("Item not in player inventory " + self.name, 0)

            # If turn-based combat is the preferred action method of the library, this really isn't necessary.
            # IGNORE class Projectile(NPC):
            # IGNORE This needs specialized collision detection.
            # def __init__(self, name, done, sprite_list, x, y):
            # super(Projectile, self).__init__(name, done, sprite_list, x, y)

            # def interact_with(self, player):
            # IGNORE Redesign for projectiles.
            # pass
