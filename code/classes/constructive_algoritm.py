from .rushhour import Rushhour
from copy import deepcopy
from .archive import Archive
from collections import deque
import sys

class Constructive(object):
    """Class that contains functions that are used in all constructive
    algoritms. """

    def hashh(self, car_list):
        """Hashes a car list (configuration of a board).
        car_list = list, contains car object of the current board
        Returns a hash of the car_list"""
        coordinates = []
        for item in car_list:
            coordinates.append(item.coordinate)
        hash_code = hash(str(coordinates))
        return hash_code

    def make_solution(self, solution):
        """Traces the solution back and returns the solution
        solution = deque(), a queue that is empty
        solution = queue
        Returns a list with the cars and their moves"""
        cursor = self.archive
        while cursor.parent:
            # while not end of solution
            solution.appendleft(cursor.move)
            cursor = self.archive_dict[cursor.parent]
        solution.append([1, [(self.game.board.entrance[0] - 1),
                        self.game.board.entrance[0]]])
        return solution

    def make_possible_children(self, parent, distance):
        """Creates a queue and puts all board states that have not yet been
        visited in the archive. Parent = list of car objects, distance = integer
        parent = list of car objects of parent board
        distance = int, distance from starting board"""
        self.game = Rushhour(parent, self.board)
        command_list = self.game.make_possible_move()
        for move in command_list:
            car_id = move[0]
            command = move[1]
            self.game.move(command, car_id, deepcopy(parent))
            child_car_list = self.game.return_car_list()
            if self.game.won():
                if self.winning(move, parent, child_car_list, distance):
                    break
            elif self.check_child(child_car_list, distance):
                self.add_to_archive(move, parent, child_car_list, distance)

    def winning(self, move, parent, child_car_list, distance):
        """If the game is won, the final board is added to the Archive and the
        solution is made.
        move = [car_id, command], contains info on the move which has been made
        parent = list of car objects of parent board
        child_car_list = list of car objects of current board
        distance = int, distance from starting board
        Returns True"""
        self.won = True
        self.archive = Archive(move, self.hashh(parent), deepcopy(child_car_list), distance)
        solution = deque()
        self.solution = self.make_solution(solution)
        self.final_board = child_car_list
        print("Congratulations, you have found a solution!")
        return True

    def return_car_list(self):
        """Returns list of car objects"""
        return self.final_board

    def spinner(self, counter):
        """Progress spinner cause its awesome"""
        # turning tables
        syms = ['\\', '|', '/', '-']
        bs = "\b"
        sym = syms[counter]
        sys.stdout.write("\b%s" % sym)
        sys.stdout.flush()
