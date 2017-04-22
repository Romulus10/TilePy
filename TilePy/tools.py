import random


def remove_newlines(x):
    """
    Extract newlines from a list.
    :param x: list of characters
    :rtype: list of characters
    """
    for y in x:
        if y == "\n":
            x.remove(x[x.index(y)])
    return x


def die_roll(dice):
    """
    Rolls a die with [sides] sides.
    :param dice: Number of sides on the die.
    :rtype: Integer from 1 to [sides]
    """
    return random.randrange(4) * dice


def calculate_damage(attack, defense):
    """
    :param attack: The attacker's attack strength.
    :param defense: The defender's chance to resist damage.
    :return: How much damage the attack will deal.
    """
    x = die_roll(attack + 1)
    print("Attack die roll: " + str(x))
    y = die_roll(defense + 1)
    print("Defense die roll: " + str(y))
    dmg = (x - y)
    print("Damage value: " + str(dmg))
    if dmg < 0:
        return 0
    else:
        return dmg
