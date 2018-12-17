from collections import deque
from code.classes.archive import Archive
from copy import deepcopy
from code.classes.rushhour import Rushhour
import heapq
from code.classes.constructive_algoritm import Constructive


class BeamSearch(Constructive):

    def __init__(self, game, final_board, beam):
        """
        Initialization method that creates a dictionary to store the graph,
        a heap as queue
        game = rushhour
        final_board = list, from a previous algorthm.
        """
        self.heap = []
        self.archive_dict = {}
        self.game = game
        self.board = game.board
        self.archive = None
        self.solution = None
        self.won = False
        self.final_car_list = final_board
        self.counter = 0
        self.beam = beam

    def run(self):
        """
        Function that iterates over the graph of parent boards and children
        It pops an archive object from the queue (heap) that has the lowest value

        returns a solution
        """
        source = self.game.return_car_list()
        distance = 0
        source_board = Archive(None, None, deepcopy(source), distance)
        self.archive_dict[self.hashh(source)] = source_board

        self.make_possible_children(source, distance + 1)

        while self.heap:
            if len(self.heap) > self.beam:
                self.heap = heapq.nsmallest(self.beam, self.heap)
            queueobject = heapq.heappop(self.heap)
            current = self.archive_dict[queueobject[1]]
            print(queueobject[0], current.distance)

            if self.won:
                print(f"The solution was found in {self.archive.distance + 1} steps.")
                return self.solution
            else:
                self.make_possible_children(current.current, current.distance + 1)
                current.current = self.hashh(current.current)
        print("No solution was found")

    def add_to_archive(self, move, parent, child_car_list, distance):
        """Adds an archive object to the archive
        move = [car_id, command], contains info on the move which has been made
        parent = list of car objects of parent board
        child_car_list = list of car objects of current board
        distance = int, distance from starting board """
        archive = Archive(move, self.hashh(parent), deepcopy(child_car_list), distance)
        value = self.value_giver(self.final_car_list, child_car_list)
        heapq.heappush(self.heap, (value, self.hashh(child_car_list)))
        self.archive_dict[self.hashh(child_car_list)] = archive

    def check_child(self, child_car_list, distance):
            return not self.hashh(child_car_list) in self.archive_dict

    def value_giver(self, final_car_list, inital_car_list):
        """Calculates a value for a board based on coordinates of cars of the
        final board and what the current board is
        final_car_list = list of car objects of the final board
        inital_car_list = list of car objects of current board
        returns a value (integer)"""
        board_value = 0
        if final_car_list:
            for car in inital_car_list:
                if car.direction == "x":
                    difference = abs(car.coordinate[0][0] - final_car_list[int(car.id) - 1].coordinate[0][0])
                    board_value += difference
                else:
                    difference = abs(car.coordinate[0][1] - final_car_list[int(car.id) - 1].coordinate[0][1])
                    board_value += difference
        return board_value

    def freeing_cars(self, current_car_list, child_car_list):
        """Heuristic for freeing other cars
        child_car_list = list of car objects of child board
        current_car_list = list of car objects of current board."""
        heur_value = 0
        current_command_list = self.game.make_possible_move_with_input(current_car_list)
        child_command_list = self.game.make_possible_move_with_input(child_car_list)
        car_id_list = []
        for move in current_command_list:
            car_id_list.append(move[0])
        for move in child_command_list:
            if move[0] in car_id_list:
                heur_value += 1
        return(heur_value)
