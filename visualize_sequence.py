# Class that visualizes a sequence of RushHour Boards

from code.classes.visualize_board import BoardVisualization
from code.classes.load_cars import LoadCars
import time
from master import Rushhour


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
        game = Rushhour(game_id)
        visual = BoardVisualization(game.board, game.car_list, game.counter)
        for move in self.sequence:
            # wait a few seconds
            time.sleep(0.5)
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


if __name__ == '__main__':
    sequence = ["5 0,1", "6 0,1", "2 3,4,5", "3 1,2", "1 0,1", "2 1,2,3", "7 1,2,3", "6 4,5", "2 3,4,5", "1 1,2", "5 4,5", "1 0,1", "3 0,1", "2 0,1,2", "7 0,1,2", "8 0,1", "4 1,2,3", "2 3,4,5", "7 1,2,3", "3 4,5", "7 3,4,5", "1 3,4", "2 0,1,2", "8 1,2", "5 0,1", "8 0,1", "2 3,4,5", "1 0,1", "2 0,1,2", "7 0,1,2", "6 0,1", "9 0,1", "2 3,4,5", "7 3,4,5", "4 3,4,5", "1 4,5"]
    visual = SequenceVisualization(sequence, "1")
