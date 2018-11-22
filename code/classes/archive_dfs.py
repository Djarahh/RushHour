class Archive(object):
    """docstring for Archive."""
    def __init__(self, move, car_list_parent, distance):
        """Initalization of the Archive object
        move = list, contains id and list of either x or y coordinates
        car_list_parent = list, contains car objects of the parent
        distance = int, dinstance to the original board"""
        self.move = move
        self.parent = car_list_parent
        self.child = None
        self.distance = distance

    def hash_parent(self, move):
        """Hash function for the car_list.
        bool = bool"""
        coordinates = []
        for car in self.parent:
            coordinates.append(car.coordinate)
        hash_code = hash(str(coordinates))
        return hash_code
