# Class that visualizes a sequence of RushHour Boards
<<<<<<< HEAD:code/visualize_sequence.py
from code.classes.load_cars import LoadCars
import os
import sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "classes"))

import tkinter as tk
from visualize_board import BoardVisualization
import time
from code.rushhour import Rushhour
=======

from code.classes.visualize_board import BoardVisualization
import time
from master import Rushhour
>>>>>>> e161c06683e519ebae0ef545ca2a4c5a7d4a2856:visualize_sequence.py


class SequenceVisualization:
    def __init__(self, sequence, game_id):
        """
        Visualizes a sequence of RushHour boards

        sequence = (a list of moves)
        start_board = (starting board)
        """

        self.sequence = sequence
        self.game_id = game_id
        self.counter = 0
        things = LoadCars("3")
        car_list = things.car_list
        board = things.board

        game = Rushhour(car_list, board)
        visual = BoardVisualization(game.board, game.car_list, game.counter)
        for move in self.sequence:
            # wait a few seconds
            time.sleep(0.5)
            # do the move
            command = move.split()
            id = command[0]
<<<<<<< HEAD:code/visualize_sequence.py
            # command = game.clean_input(command[1])
=======
            command = game.clean_input(command[1])
            print(command)
>>>>>>> e161c06683e519ebae0ef545ca2a4c5a7d4a2856:visualize_sequence.py
            game.move(command, id)

            # update the visualization
            visual.update(game.car_list, game.counter)

        # enter the main loop
        visual.done()


if __name__ == '__main__':
    sequence = ["5 0,1", "6 0,1", "2 3,4,5", "3 1,2", "1 0,1", "2 1,2,3", "7 1,2,3", "6 4,5", "2 3,4,5", "1 1,2", "5 4,5", "1 0,1", "3 0,1", "2 0,1,2", "7 0,1,2", "8 0,1", "4 1,2,3", "2 3,4,5", "7 1,2,3", "3 4,5", "7 3,4,5", "1 3,4", "2 0,1,2", "8 1,2", "5 0,1", "8 0,1", "2 3,4,5", "1 0,1", "2 0,1,2", "7 0,1,2", "6 0,1", "9 0,1", "2 3,4,5", "7 3,4,5", "4 3,4,5", "1 4,5"]
    visual = SequenceVisualization(sequence, "1")
