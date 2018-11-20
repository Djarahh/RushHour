class Archive(object):
    """docstring for Archive."""
    def __init__(self, move, car_list_parent, distance):
        """Initalization of the Archive object
        move = list, contains id and list of either x or y coordinates
        car_list_parent = list, contains car objects of the parent
        distance = int, dinstance to the original board"""
        self.move = move
        self.parent = car_list_parent
        self.child = car_list_self
        self.distance = 0

    def children_made(self, bool):
        """Hash function for the car_list.
        bool = bool"""
        if bool:
            self.parent = hash(self.parent)
