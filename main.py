from copy import deepcopy
import code as cd
import argparse


def main(game_id, algorithm, beam, visualize):
    """
    Uses algorithms to solve a RushHour board.
    Makes .txt files with the solution.
    Visualizes the solution.
    game_id = string (number of gameboard)
    algorithm = string(algorihm that is being put in by user)
    """
    # Load the cars and the board
    things = cd.cs.LoadCars(game_id)
    car_list = things.car_list
    board = things.board

    # Initiate a RushHour game and an empty solution
    rushhour = cd.cs.Rushhour(deepcopy(car_list), deepcopy(board))
    solution = []

    if algorithm == "random":
        # # Let the randomize algorithm run and return a solution
        A = cd.alg.Randomize(deepcopy(rushhour), deepcopy(car_list))
        solution = A.run()

    elif algorithm == "best" or algorithm == "beam":
        # Let the randomize algorithm run and return a solution for bestfs
        A = cd.alg.Randomize(deepcopy(rushhour), deepcopy(car_list))
        solution = A.run()

        # Save the random solution
        final_board = A.game.return_car_list()
        cd.cs.TxtSolution(game_id, solution, algorithm)

        if algorithm == "best":
            # Run the Best First Search algorithm
            rush = cd.cs.Rushhour(deepcopy(car_list), deepcopy(board))
            B = cd.alg.BestFirst(rush, final_board)
            solution = B.run()

        else:
            # let the BeamSearch algorithm work
            B = cd.alg.BeamSearch(deepcopy(rushhour), final_board, beam)
            solution = B.run()

    elif algorithm == "bfs":
        # Let the BFS algorithm work
        B = cd.alg.Graph(deepcopy(rushhour))
        solution = B.run()

    elif algorithm == "dfs":
        # Let the DFS algorithm work it
        C = cd.alg.Tree(deepcopy(rushhour))
        solution = C.run()

    elif algorithm == "bnb":
        # Branch and Bound algorithm
        D = cd.alg.Branches(deepcopy(rushhour))
        solution = D.run()

    if solution:
        # Make a .txt file with the solution
        cd.cs.TxtSolution(game_id, solution, algorithm)

        if visualize == "yes" or visualize == "y":
            # Visualize the solution that the algorithm made
            if algorithm == "random":
                speed = 0.0005
            else:
                speed = 0.1

            cd.vis.SequenceVisualization(game_id, rushhour, algorithm, speed)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Solves rushhour boards.')

    parser.add_argument("-b", "--board", metavar='board', type=int,
                        help='choose a board with the following choices [1, 2,\
                        3, 4, 5, 6, 12]',
                        default=1)
    parser.add_argument("-be", "--beam", nargs="?", metavar="width", type=int,
                        help="the width of the beamsearch (default = 100)",
                        default=100)

    parser.add_argument('-a', "--algorithm", metavar='algorithm', nargs=1,
                        help='choose (an) algoritm(s) with the following \
                        choices ["bfs", "best", "dfs", "bnb", "random", "beam"]',
                        default="random")

    parser.add_argument("-vis", "--visualize", nargs="?", metavar="visualize", type=str,
                        help="turns visualize on or off (choose from yes (y) or no (n))",
                        default="yes")

    args = parser.parse_args()
    print(args.board, args.algorithm[0], args.beam, args.visualize)

    main(args.board, args.algorithm[0], args.beam, args.visualize)
