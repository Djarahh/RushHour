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
            print(f"Stack: {len(self.stack)}")
        return print(self.solution)

    def make_possible_babies(self, parent, distance):
        self.game = Rushhour(parent, self.board)
        command_list = self.game.make_possible_move()
        # print(command_list)
        for move in command_list:
            car_id = move[0]
            command = move[1]
            self.game.move(command, car_id, deepcopy(parent))
            child_car_list = self.game.return_car_list()
            if self.game.won():
                print(self.bound)
                time.sleep(3)
                self.archive = Archive(move, deepcopy(parent), deepcopy(child_car_list), distance)
                self.update_bound(distance)
                self.solution = self.make_solution()
            else:
                self.check_baby(child_car_list, distance)
                archive = Archive(move, deepcopy(parent), deepcopy(child_car_list), distance)
                self.stack.appendleft(archive)
                self.archive_dict[self.hashh(child_car_list)] = archive

    def check_baby(self, child_car_list, distance):
        if self.hashh(child_car_list) in self.archive_dict:
            check = self.archive_dict[self.hashh(child_car_list)]
            if check.distance > distance:
                return True
        else:
            return True

    def hashh(self, car_list):
        coordinates = []
        for item in car_list:
            coordinates.append(item.coordinate)
        hash_code = hash(str(coordinates))
        return hash_code

    def update_bound(self, distance):
        self.bound = distance

    def make_solution(self):
        solution = deque()
        cursor = self.archive
        while True:
            solution.appendleft(cursor.move)
            cursor = self.archive_dict[self.hashh(cursor.parent)]
            if cursor.parent == None:
                solution.append([1, [4,5]])
                break
        return solution
