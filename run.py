from code.classes.rushhour import Rushhour
from code.algorithms.random_possible_moves import Randomize
from code.algorithms.BFS_solution import Graph
from code.algorithms.DFS_solution import Tree
from code.algorithms.Branch_and_Bound import Branches
# from code.algorithms.Iterative_deepening_DFS import Iterative
from code.classes.load_cars import LoadCars
# from code.classes.load_solution import LoadSolution
# from code.algorithms.Random_compare import Find_pattern
from code.algorithms.Best_first import BestFirst
from code.algorithms.Beam_search import BeamSearch
# from code.visualization.visualize_board import BoardVisualization
# from code.visualization.visualize_sequence import SequenceVisualization
# from code.classes.solution_txt import TxtSolution
from copy import deepcopy
# from timeit import Timer
# from code.algorithms.iterative import Iterative


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

    # # # Let the randomize algorithm run and return a solution
    A = Randomize(deepcopy(rushhour), deepcopy(car_list))
    solution = A.run()
    solved_board = A.game.return_car_list()
    algorithm = "RANDOM"

    # Let the BFS algorithm work
    # B = Graph(deepcopy(rushhour))
    # solution = B.run()
    # algorithm = "BFS"

    # # Let the DFS algorithm work it
    # C = Tree(deepcopy(rushhour))
    # solution = C.run()
    # algorithm = "DFS"

    # # # Branch and Bound algorithm
    # D = Branches(deepcopy(rushhour))
    # solution = D.run()
    # algorithm = "BNB"

    # # Iterative deepening DFS
    # E = Iterative(deepcopy(rushhour))
    # solution = E.bnb()
    # algorithm = "IDDFS"

    # # solution = []
    # F = Find_pattern(deepcopy(rushhour), solution)
    # # F.find_pattern(1)
    #
    # s = LoadSolution(game_id)
    # solved_board = s.car_list
    #
    # G = BestFirst(deepcopy(rushhour), solved_board)
    # solution = G.run()
    # algorithm = "BEST"

    # H = BeamSearch(deepcopy(rushhour), solved_board, 100)
    # solution = H.run()
     # algorithm = "BEST"
    #
    # # # Make a .txt file with the solution
    # TxtSolution(game_id, solution, algorithm)

    # # Visualize the solution that the algorithm made
    # SequenceVisualization(game_id, rushhour, algorithm)



if __name__ == "__main__":
    main("4")
