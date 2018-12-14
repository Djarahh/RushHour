from collections import deque
from code.classes.archive import Archive
from copy import deepcopy
from code.classes.rushhour import Rushhour
from code.classes.constructive_algoritm import Constructive



class Tree(Constructive):
    def __init__(self, game):
        """
        Initializes a tree object to use for depth first search
        """
        self.stack = deque()
        self.game = game
        self.board = game.board
        self.archive_dict = {}
        self.solution = None
        self.won = False

    def run(self):
        """Searches the tree untill a solution is found, pulling from a stack"""
        source = self.game.return_car_list()
        distance = 0
        source_board = Archive(None, None, deepcopy(source), distance)
        self.archive_dict[self.hashh(source)] = source_board

        self.make_possible_children(source, distance + 1)
        # print(f"Stack: {len(self.stack)}")

        while not self.won:
            current = self.stack.popleft()
            self.make_possible_children(current.current, current.distance + 1)
        return self.solution


    def add_to_archive(self, move, parent, child_car_list, distance):
        archive = Archive(move, self.hashh(parent), deepcopy(child_car_list), distance)
        self.archive_dict[self.hashh(child_car_list)] = archive
        self.put(archive)

    def check_child(self, child_car_list, distance):
        if self.hashh(child_car_list) in self.archive_dict:
            check = self.archive_dict[self.hashh(child_car_list)]
            return check.distance > distance
        else:
            return True
    def put(self, archive):
        self.stack.appendleft(archive)

    def hashh(self, car_list):
        coordinates = []
        for item in car_list:
            coordinates.append(item.coordinate)
        hash_code = hash(str(coordinates))
        return hash_code
