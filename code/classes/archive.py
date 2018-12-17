from copy import deepcopy

class Archive(object):
    def __init__(self, move, car_list_parent, current, distance):
        """
        Initalization of the Archive object

        move = list, contains id and list of either x or y coordinates
        car_list_parent = list, contains car objects of the parent
        distance = int, dinstance to the original board
        """
        self.move = move
        self.parent = car_list_parent
        self.current = current
        self.distance = distance
