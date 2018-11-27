from code.rushhour import Rushhour
from code.algorithms.random_possible_moves import Randomize
from code.algorithms.BFS_archive_check import Graph
# from code.algorithms.DFS import Tree
from code.classes.load_cars import LoadCars
from code.visualization.visualize_sequence import SequenceVisualization
from code.classes.solution_txt import TxtSolution
from code.algorithms.iterative import Iterative
from copy import deepcopy


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

    # Let the randomize algorithm run and return a solution
<<<<<<< HEAD
    A = Randomize(rushhour)
    solution = A.randomize()
    final_car_list = rushhour.return_car_list()
    # use iterative function
    rushhour.return_car_list
    rushhour = Rushhour(deepcopy(car_list), deepcopy(board))
    I = Iterative(deepcopy(car_list), final_car_list, rushhour)
=======
    # A = Randomize(deepcopy(rushhour))
    # solution = A.randomize()

>>>>>>> fe7e94c126cec9e8f72f0b6219df2de27ad9f380
    # Let the BFS algorthm work
<<<<<<< HEAD
    B = Graph(rushhour)
=======
    B = Graph(deepcopy(rushhour))
>>>>>>> d52e56a2a632dc66ff5ecf9ab11a0a6f21e8c471
    B.bfs()

    # # Let the DFS algorithm work it
    # C = Tree(rushhour)
    # C.dfs()

<<<<<<< HEAD
    # # Make a .txt file with the solution
    # TxtSolution(game_id, solution)
    # #
    # # # Visualize the solution that the algorithm made
=======
    # Make a .txt file with the solution
    # TxtSolution(game_id, solution)
    #
    # # Visualize the solution that the algorithm made
>>>>>>> d52e56a2a632dc66ff5ecf9ab11a0a6f21e8c471
    # SequenceVisualization(game_id, rushhour)


if __name__ == "__main__":
    main("7")
