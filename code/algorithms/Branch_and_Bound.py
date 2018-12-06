from collections import deque
from code.classes.archive import Archive
from copy import deepcopy
from code.rushhour import Rushhour
import time


class Branches(object):
    def __init__(self, game):
        """
        Initializes a tree object to use for depth first search
        """
        self.stack = deque()
        self.game = game
        self.board = game.board
        self.archive_dict = {}
        self.solution = None
        self.bound = 180

    def bnb(self):
        """
        Searches the tree untill a solution is found, and resets the bound to
        the depth of that solution. And starts iterating over the tree again
        """
        source = self.game.return_car_list()
        distance = 0
        source_board = Archive(None, None, deepcopy(source), distance)
        self.archive_dict[self.hashh(source)] = source_board

        self.make_possible_babies(source, distance + 1)
        # print(f"Stack: {len(self.stack)}")

        while self.stack:
            current = self.stack.popleft()
            while current.distance > self.bound:
                current = self.stack.popleft()
            self.make_possible_babies(current.current, current.distance + 1)
            # print(f"Stack: {len(self.stack)}")
        print(f"Length archive:{len(self.archive_dict)}")
        return self.solution

    def make_possible_babies(self, parent, distance):
        """Creates a stack and puts all board states that have not yet been
        visited in the archive.
        Parent = list of car objects
        distance = integer """
        self.game = Rushhour(parent, self.board)
        command_list = self.game.make_possible_move()
        # print(command_list)
        for move in command_list:
            car_id = move[0]
            command = move[1]
            self.game.move(command, car_id, deepcopy(parent))
            child_car_list = self.game.return_car_list()
            if self.game.won():
                self.archive = Archive(move, deepcopy(parent), deepcopy(child_car_list), distance)
                self.update_bound(distance)
                print(f"Bound: {self.bound}")
                self.solution = self.make_solution()
                time.sleep(2)
            elif self.check_baby(child_car_list, distance):
                archive = Archive(move, deepcopy(parent), deepcopy(child_car_list), distance)
                self.stack.appendleft(archive)
                self.archive_dict[self.hashh(child_car_list)] = archive

    def check_baby(self, child_car_list, distance):
        """Checks if the boards of children are already in the archive"""
        if self.hashh(child_car_list) in self.archive_dict:
            check = self.archive_dict[self.hashh(child_car_list)]
            if check.distance > distance:
                return True
        else:
            return True

    def hashh(self, car_list):
        """Hashes the coordinates of a board
        car_list = list of car objects"""
        coordinates = []
        for item in car_list:
            coordinates.append(item.coordinate)
        hash_code = hash(str(coordinates))
        return hash_code

    def update_bound(self, distance):
        """Updates the bound"""
        self.bound = distance - 30

    def make_solution(self):
        """Tracks the solution back and returns the solution"""
        solution = deque()
        cursor = self.archive
        while True:
            solution.appendleft(cursor.move)
            cursor = self.archive_dict[self.hashh(cursor.parent)]
            if cursor.parent == None:
                solution.append([1, [(self.game.board.entrance[0] - 1), self.game.board.entrance[0]]])
                break
        return solution
