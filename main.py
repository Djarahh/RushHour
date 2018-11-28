from code.rushhour import Rushhour
from code.algorithms.random_possible_moves import Randomize
from code.algorithms.BFS_solution import Graph
from code.algorithms.DFS_solution import Tree
from code.algorithms.Branch_and_Bound import Branches
from code.classes.load_cars import LoadCars
from code.visualization.visualize_sequence import SequenceVisualization
from code.classes.solution_txt import TxtSolution
from copy import deepcopy
from code.algorithms.value_giver_best_first import ValueGiver


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

<<<<<<< HEAD
    # Let the randomize algorithm run and return a solution
    # A = Randomize(deepcopy(rushhour))
    # solution = A.randomize()
    # algorithm = "RANDOM"

    # # Let the BFS algorthm work
    B = Graph(deepcopy(rushhour))
    solution = B.bfs()
    algorithm = "BFS"
=======
    # # Let the randomize algorithm run and return a solution
    # A = Randomize(deepcopy(rushhour))
    # solution = A.randomize()
    # algorithm = "RANDOM"
<<<<<<< HEAD
=======
=======
    A = Randomize((rushhour))
    solution = A.randomize()
    #algorithm = "RANDOM"
    final_board = rushhour.return_car_list()
    # use this algorithm for the final board of rushhour
    rush = Rushhour(deepcopy(car_list), deepcopy(board))
<<<<<<< HEAD
    B = ValueGiver(deepcopy(car_list), deepcopy(final_board), rush)
    w = B.compare_i_f()
    print(B.board_value)
=======
    B = Iterative(deepcopy(car_list), deepcopy(final_board), rush)
>>>>>>> 76f930308c4dcade1c2ccc80afaa929d78ce3995
>>>>>>> 8ba99cd4484d0ac0fb6e39c76693c27df27be23c
>>>>>>> f456a447901f1e010fb1821b47c25bdd58975850

    # # Let the BFS algorithm work
    # B = Graph(deepcopy(rushhour))
    # solution = B.bfs()
    # algorithm = "BFS"
>>>>>>> 14a8d418e52b3ac4cb9fbcf284da88279e1398b7

    # Let the DFS algorithm work it
    # C = Tree(deepcopy(rushhour))
    # solution = C.dfs()
    # algorithm = "DFS"

<<<<<<< HEAD
=======
<<<<<<< HEAD

=======
<<<<<<< HEAD
>>>>>>> f456a447901f1e010fb1821b47c25bdd58975850
    # # Branch and Bound algorithm
    D = Branches(deepcopy(rushhour))
    solution = D.bnb()
    # algorithm = "BNB"

    # # Make a .txt file with the solution
    # TxtSolution(game_id, solution, algorithm)
    #
    # # Visualize the solution that the algorithm made
    # SequenceVisualization(game_id, rushhour, algorithm)

if __name__ == "__main__":
    main("2")
<<<<<<< HEAD
=======
=======
>>>>>>> 14a8d418e52b3ac4cb9fbcf284da88279e1398b7
    # # Make a .txt file with the solution
    # TxtSolution(game_id, solution)

    # # Visualize the solution that the algorithm made
    # SequenceVisualization(game_id, rushhour)
<<<<<<< HEAD

    # Make a .txt file with the solution
    TxtSolution(game_id, solution, algorithm)
=======
>>>>>>> 14a8d418e52b3ac4cb9fbcf284da88279e1398b7

    # Visualize the solution that the algorithm made
    # SequenceVisualization(game_id, rushhour, algorithm)


if __name__ == "__main__":
<<<<<<< HEAD
    main("1")
=======
    main("7")
>>>>>>> 76f930308c4dcade1c2ccc80afaa929d78ce3995
>>>>>>> 14a8d418e52b3ac4cb9fbcf284da88279e1398b7
>>>>>>> f456a447901f1e010fb1821b47c25bdd58975850
