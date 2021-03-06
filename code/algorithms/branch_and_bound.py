from collections import deque
from code.classes.archive import Archive
from copy import deepcopy
from code.classes.constructive_algoritm import Constructive
import time


class Branches(Constructive):
    def __init__(self, game, bound, updatebound):
        """
        Initializes a tree object to use for depth first search

        game = rushhour object
        bound = interger
        updatebound = integers
        """
        self.stack = deque()
        self.game = game
        self.board = game.board
        self.archive_dict = {}
        self.solution = None
        self.bound = bound
        self.updatebound = updatebound

    def run(self):
        """
        Searches the tree untill a solution is found, and resets the bound to
        the depth of that solution. And starts iterating over the tree again

        returns the solution
        """
        source = self.game.return_car_list()
        distance = 0
        source_board = Archive(None, None, deepcopy(source), distance)
        self.archive_dict[self.hashh(source)] = source_board
        self.make_possible_children(source, distance + 1, False)

        # print statements and counter for the spinner
        print("running...")
        counter_spinner = 0
        counter_bound = 0
        while self.stack:
            counter_spinner += 1
            self.spinner(counter_spinner % 4)
            current = self.stack.popleft()
            if current.distance == self.bound:
                counter_bound += 1
            while current.distance > self.bound:
                current = self.stack.popleft()
            self.make_possible_children(current.current, current.distance + 1,
                                        False)
        print(f"the bound was reached {counter_bound} times")
        return self.solution

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

    def put(self, archive):
        """
        Adds archive object to stack

        archive = archive object
        """
        self.stack.appendleft(archive)

    def winning(self, move, parent, child_car_list, distance, deepest):
        """
        If the game is won, the final board is added to the Archive and the
        solution is made. The bound is also updated

        move = [car_id, command], contains info on the move which has been made
        parent = list of car objects of parent board
        child_car_list = list of car objects of current board
        distance = int, distance from starting board
        Returns False
        """
        self.archive = Archive(move, self.hashh(parent),
                               deepcopy(child_car_list), distance)
        self.update_bound(distance)
        print(f"Bound: {self.bound}")
        solution = deque()
        self.solution = self.make_solution(solution)
        time.sleep(2)
        return False

    def update_bound(self, distance):
        """
        Updates the bound

        distance = int, steps from the initial board
        """
        self.bound = distance - self.updatebound
