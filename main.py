from code.rushhour import Rushhour
from code.algorithms.random_possible_moves import Randomize
# from code.algorithms.BFS_archive_check import Graph
from code.algorithms.BFS_solution import Graph
# from code.algorithms.DFS import Tree
from code.classes.load_cars import LoadCars
from code.visualization.visualize_sequence import SequenceVisualization
from code.classes.solution_txt import TxtSolution
from copy import deepcopy
from code.algorithms.iterative import Iterative


def main(game_id):
    """
    Uses algorithms to solve a RushHour board.
    Makes .txt files with the solution.
    Visualizes the solution.
    game_id = string (number of gameboard)
    """
    # Load the cars and the board
    things = LoadCars(game_id)
    car_list = things.car_list
    board = things.board

    # Initiate a RushHour game
    rushhour = Rushhour(deepcopy(car_list), deepcopy(board))

    # # Let the randomize algorithm run and return a solution
    A = Randomize((rushhour))
    solution = A.randomize()
    #algorithm = "RANDOM"
    final_board = rushhour.return_car_list()
    # use this algorithm for the final board of rushhour
    rush = Rushhour(deepcopy(car_list), deepcopy(board))
    B = Iterative(deepcopy(car_list), deepcopy(final_board), rush)

    # Let the BFS algorithm work
    # B = Graph(deepcopy(rushhour))
    # solution = B.bfs()
    # algorithm = "BFS"

    # # Let the DFS algorithm work it
    # C = Tree(rushhour)
    # C.dfs()

    # # Make a .txt file with the solution
    # TxtSolution(game_id, solution)

    # # Visualize the solution that the algorithm made
    # SequenceVisualization(game_id, rushhour)

    # Visualize the solution that the algorithm made
    # SequenceVisualization(game_id, rushhour, algorithm)


if __name__ == "__main__":
    main("7")
