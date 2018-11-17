from code.rushhour import Rushhour
# from code.algorithms.random_things import Randomize
from code.algorithms.random_possible_moves import Randomize
from code.classes.load_cars import LoadCars
from code.classes.visualize_sequence import SequenceVisualization


def main(game_id):
    things = LoadCars(game_id)
    car_list = things.car_list
    board = things.board
    # how to import willekeurig
    rushhour = Rushhour(car_list, board)
    Randomize(rushhour)

    # Visualize the solution that the algorithm made
    SequenceVisualization(game_id)


if __name__ == "__main__":
    main("2")
