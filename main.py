from copy import deepcopy
import code as cd


def main(game_id):
    """
    Uses algorithms to solve a RushHour board.
    Makes .txt files with the solution.
    Visualizes the solution.
    game_id = string (number of gameboard)
    """
    # Load the cars and the board
    things = cd.cs.LoadCars(game_id)
    car_list = things.car_list
    board = things.board

    # Initiate a RushHour game
    rushhour = cd.cs.Rushhour(deepcopy(car_list), deepcopy(board))

    # # Let the randomize algorithm run and return a solution
    # A = cd.alg.Randomize(deepcopy(rushhour), deepcopy(car_list))
    # solution= A.randomize()
    # algorithm = "RANDOM"
    # #
    # final_board = A.game.return_car_list()
    #
    # for car in final_board:
    #     print(car.id)
    #     print(car.coordinate)
    # cd.cs.TxtSolution(game_id, solution, algorithm)
    #
    # # s = LoadSolution(game_id)
    # # solved_board = s.car_list
    # #
    # rush = cd.cs.Rushhour(deepcopy(car_list), deepcopy(board))
    # B = cd.alg.BestFirst(rush, final_board)
    # solution = B.bfs()
    # algorithm = "BEST"
    #
    # s = cd.cs.LoadSolution(game_id)
    # solved_board = s.car_list

    # Let the BFS algorithm work
    # B = cd.alg.Graph(deepcopy(rushhour))
    # solution = B.bfs()
    # algorithm = "BFS"


    # Let the DFS algorithm work it
    C =  cd.alg.Tree(deepcopy(rushhour))
    solution = C.dfs()
    print(len(solution))
    algorithm = "DFS"


    # # Branch and Bound algorithm
    # D = cd.alg.Branches(deepcopy(rushhour))
    # solution = D.bnb()
    # algorithm = "BNB"


    # Make a .txt file with the solution
    cd.cs.TxtSolution(game_id, solution, algorithm)

    # Visualize the solution that the algorithm made
    # SequenceVisualization(game_id, rushhour, algorithm)

if __name__ == "__main__":
<<<<<<< HEAD
    main("6")
=======
    main("4")
>>>>>>> ab4c662d6f84aa76a2a108c3b24c4e4e0ad64541
