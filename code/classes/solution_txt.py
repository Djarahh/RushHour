class TxtSolution(object):
    def __init__(self, game_id, solution, algorithm):
        """
        Makes a .txt file from the solution found by the algorithm

        game_id = string (number of the gameboard)
        solution = list of moves
        move = [car_id, [command]]
        """
        self.game_id = game_id
        self.solution = solution
        self.algorithm = algorithm
        self.make_file(f"results/{self.algorithm}solution{self.game_id}.txt")

    def make_file(self, output_file):
        """
        Opens a .txt file with the solution

        output_file = string (filename of new .txt file)
        """
        with open(output_file, 'w') as output:
            # write a string of the car_id + command in "car_id command"
            # with command = a,b
            for move in self.solution:
                car_id = move[0]
                command = move[1]
                if len(command) > 2:
                    output.write(f"{car_id} {command[0]},{command[1]},{command[2]}\n")
                else:
                    output.write(f"{car_id} {command[0]},{command[1]}\n")
