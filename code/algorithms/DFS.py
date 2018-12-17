from collections import deque
from code.classes.archive import Archive
from copy import deepcopy
from code.classes.constructive_algoritm import Constructive


class Tree(Constructive):
    def __init__(self, game):
        """
        Initializes a tree object to use for depth first search
        game = rushhour object
        """
        self.stack = deque()
        self.game = game
        self.board = game.board
        self.archive_dict = {}
        self.solution = None
        self.won = False

    def run(self):
        """
        Searches the tree untill a solution is found, pulling from a stack
        """
        source = self.game.return_car_list()
        distance = 0
        source_board = Archive(None, None, deepcopy(source), distance)
        self.archive_dict[self.hashh(source)] = source_board

        self.make_possible_children(source, distance + 1, False)

        # print statements and counter for the spinner
        print("running...")
        counter_spinner = 0

        while not self.won:
            counter_spinner += 1
            self.spinner(counter_spinner % 4)
            current = self.stack.popleft()
            self.make_possible_children(current.current, current.distance + 1,
                                        False)

        print(f"the solution was found in {current.distance + 1} steps")
        return self.solution

    def add_to_archive(self, move, parent, child_car_list, distance):
        """
        Creates archive object and adds it to the archive.

        move = [car_id, command], contains info on the move which has been made
        parent = list of car objects of parent board
        child_car_list = list of car objects of current board
        distance = int, distance from starting board
        """
        archive = Archive(move, self.hashh(parent), deepcopy(child_car_list),
                          distance)
        self.archive_dict[self.hashh(child_car_list)] = archive
        self.put(archive)

    def check_child(self, child_car_list, distance):
        """
        Checks if the child is in the archive

        child_car_list = list of car objects of current board
        distance = int, distance from starting board
        Returns the distance (if child in archive)
        Returns (else) True
        """
        if self.hashh(child_car_list) in self.archive_dict:
            check = self.archive_dict[self.hashh(child_car_list)]
            return check.distance > distance
        else:
            return True

    def put(self, archive):
        """
        Adds archive object to stack

        archive = archive object
        """
        self.stack.appendleft(archive)
