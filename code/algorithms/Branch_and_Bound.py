from collections import deque
from code.classes.archive import Archive
from copy import deepcopy
from code.classes.rushhour import Rushhour
from code.classes.constructive_algoritm import Constructive
import time


class Branches(Constructive):
    def __init__(self, game):
        """
        Initializes a tree object to use for depth first search
        """
        self.stack = deque()
        self.game = game
        self.board = game.board
        self.archive_dict = {}
        self.solution = None
        self.bound = 40

    def bnb(self):
        """
        Searches the tree untill a solution is found, and resets the bound to
        the depth of that solution. And starts iterating over the tree again
        """
        source = self.game.return_car_list()
        distance = 0
        source_board = Archive(None, None, deepcopy(source), distance)
        self.archive_dict[self.hashh(source)] = source_board

        self.make_possible_children(source, distance + 1)
        # print(f"Stack: {len(self.stack)}")

        while self.stack:
            current = self.stack.popleft()
            while current.distance > self.bound:
                current = self.stack.popleft()
            self.make_possible_children(current.current, current.distance + 1)
            # print(f"Stack: {len(self.stack)}")
        print(f"Length archive:{len(self.archive_dict)}")
        return self.solution

    def check_child(self, child_car_list, distance):
        """Checks if the boards of children are already in the archive"""
        if self.hashh(child_car_list) in self.archive_dict:
            check = self.archive_dict[self.hashh(child_car_list)]
            return check.distance > distance
        else:
            return True

    def put(self, archive):
        self.stack.appendleft(archive)

    def winning(self, move, parent, child_car_list, distance):
        print("I didn't Broke")

        self.archive = Archive(move, self.hashh(parent), deepcopy(child_car_list), distance)
        self.update_bound(distance)
        print(f"Bound: {self.bound}")
        solution = deque()
        self.solution = self.make_solution(solution)
        time.sleep(2)
        return False

    def update_bound(self, distance):
        """Updates the bound"""
        self.bound = distance - 30
