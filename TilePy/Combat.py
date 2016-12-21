class StatsEnabledObject(object):
    """
    Creates a Character object which can be used in turn-based combat or in tracking character stats.
    """

    # For use in turn-based combat. I think I'll use that as the preferred combat system.
    def __init__(self, health, energy, attack, defense, speed):
        """
        StatsEnabledObject constructor. In games that will use the default combat system, the default combat object may
        be extended to add any stats needed by the game.

        :param health: Determines whether the object is dead or alive.
        :param energy: May be used for special actions.
        :param attack: How much damage we can do.
        :param defense: How much damage we can withstand.
        :param speed: Affects how quickly we'll be able to attack.
        """
        self.health = health
        self.energy = energy
        self.attack = attack
        self.defense = defense
        self.speed = speed
