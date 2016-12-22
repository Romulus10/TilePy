class MapGate(object):
    def __init__(self, pos_x, pos_y, on_map, to_map):
        """
        :param pos_x: Location of the gate on the x axis
        :param pos_y: Location of the gate on the y axis
        :param on_map: Which map the entrance is connected to
        :param to_map: The map the gate points to
        """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.on_map = on_map
        self.to_map = to_map
