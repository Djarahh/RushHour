from code.rushhour import Rushhour
from code.algorithms.random_possible_moves import Randomize
from code.algorithms.BFS_solution import Graph
from code.algorithms.DFS_solution import Tree
from code.algorithms.Branch_and_Bound import Branches
from code.classes.load_cars import LoadCars
from code.visualization.visualize_sequence import SequenceVisualization
from code.classes.solution_txt import TxtSolution
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
    rushhour = Rushhour(car_list, board)

    # # Let the randomize algorithm run and return a solution
    # A = Randomize(deepcopy(rushhour))
    # solution = A.randomize()
    # algorithm = "RANDOM"

    # # Let the BFS algorthm work
    # B = Graph(deepcopy(rushhour))
    # solution = B.bfs()
    # algorithm = "BFS"

    # # Let the DFS algorithm work it
    # C = Tree(deepcopy(rushhour))
    # solution = C.dfs()
    # algorithm = "DFS"

    # # Branch and Bound algorithm
    # D = Branches(deepcopy(rushhour))
    # solution = D.bnb()
    # algorithm = "BNB"

    # # Make a .txt file with the solution
    # TxtSolution(game_id, solution, algorithm)
    #
    # # Visualize the solution that the algorithm made
    # SequenceVisualization(game_id, rushhour, algorithm)

if __name__ == "__main__":
    main("2")
