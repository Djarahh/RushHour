# Class that visualizes a sequence of RushHour Boards

from code.visualization.visualize_board import BoardVisualization
import time


class SequenceVisualization:
    def __init__(self, game_id, game, algorithm):
        """
        Visualizes a sequence of RushHour boards

        game_id = string (number of the gameboard)
        """

        self.algorithm = algorithm
        self.sequence = self.load_sequence(f"results/{self.algorithm}solution{game_id}.txt")
        self.game_id = game_id
        self.counter = 0
        game = game
        visual = BoardVisualization(game)
        for move in self.sequence:
            # wait a few seconds
            time.sleep(0.1)
            # do the move
            command = move.split()
            id = command[0]
            command = self.clean_input(command[1])
            game.move(command, id, game.car_list)
            self.counter += 1

            # update the visualization
            visual.update(game.car_list, self.counter)

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

    def clean_input(self, command):
        """
        Converts input to usable list of integers

        command = string (a, b)
        """
        command = command.split(",")
        command_clean = []
        for i in command:
            command_clean.append(int(i))
        return command_clean
