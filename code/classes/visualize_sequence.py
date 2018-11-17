# Class that visualizes a sequence of RushHour Boards

from code.classes.visualize_board import BoardVisualization
import time
from master import Rushhour


class SequenceVisualization:
    def __init__(self, game_id):
        """
        Visualizes a sequence of RushHour boards

        game_id = string (number of the gameboard)
        """

        self.sequence = self.load_sequence(f"results/solution{game_id}.txt")
        self.game_id = game_id
        self.counter = 0
        game = Rushhour(game_id)
        visual = BoardVisualization(game.board, game.car_list, game.counter)
        for move in self.sequence:
            # wait a few seconds
            time.sleep(0.2)
            # do the move
            command = move.split()
            id = command[0]
            command = game.clean_input(command[1])
            print(command)
            game.move(command, id)

            # update the visualization
            visual.update(game.car_list, game.counter)

        # enter the main loop
        visual.done()

    def load_sequence(self, filename):
        """
        Loads in the sequence that leads to the solution of a game

        filename = string (filename of the solutions .txt file)
        """
        sequence = []

        with open(filename, 'r') as file:
            for text_line in file:
                sequence.append(text_line.strip())
        return sequence
