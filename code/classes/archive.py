class Archive(object):
    """docstring for Archive."""
    def __init__(self, move, car_list_parent, distance):
        self.move = move
        self.parent = car_list_parent
        self.child = "None"
        self.distance = 0

    def children_made(self, bool):
        if bool:
            self.parent = hash(self.parent)
