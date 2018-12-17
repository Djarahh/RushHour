from collections import deque
from code.classes.archive import Archive
from copy import deepcopy
from code.classes.rushhour import Rushhour
from code.classes.constructive_algoritm import Constructive
import heapq


class BestFirst(Constructive):

    def __init__(self, game, final_board):
        """Initialization method that creates a dictionary to store graph, a
        heap as queue
        game = rushhour
        final_board = list, from a previous algorthm."""
        self.heap = []
        self.archive_dict = {}
        self.game = game
        self.board = game.board
        self.archive = None
        self.solution = None
        self.won = False
        self.final_car_list = final_board
        self.counter = 0

    def run(self):
        """Function that iterates over the graph of parent boards and children
        It pops an archive object from the queue (heap) has the lowest value"""
        source = self.game.return_car_list()
        distance = 0
        source_board = Archive(None, None, deepcopy(source), distance)
        self.archive_dict[self.hashh(source)] = source_board

        self.make_possible_children(source, distance + 1, False)

        # list for keeping track of dept
        depth_list = [0]

        # print statements and counter for the spinner
        print("running...")
        counter_spinner = 0
        while self.heap:
            counter_spinner += 1
            self.spinner(counter_spinner % 4)
            queueobject = heapq.heappop(self.heap)
            current = self.archive_dict[queueobject[1]]

            if self.won:
                print(f"The solution was found in {self.archive.distance + 1} steps.")
                return self.solution
            else:
                self.make_possible_children(current.current, current.distance + 1, max(depth_list))
                current.current = self.hashh(current.current)

            if current.distance not in depth_list:
                depth_list.append(current.distance)
                print(f"Deepest point: {current.distance}")
        print("No solution was found")

    def add_to_archive(self, move, parent, child_car_list, distance):
        archive = Archive(move, self.hashh(parent), deepcopy(child_car_list), distance)
        value = self.value_giver(self.final_car_list, child_car_list)
        heapq.heappush(self.heap, (value, self.hashh(child_car_list)))
        self.archive_dict[self.hashh(child_car_list)] = archive

    def check_child(self, child_car_list, distance):
            return not self.hashh(child_car_list) in self.archive_dict

    def value_giver(self, final_car_list, inital_car_list):
        """Calculates the difference between xi and xf"""
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
        """Heuristic for freeing other cars"""
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
