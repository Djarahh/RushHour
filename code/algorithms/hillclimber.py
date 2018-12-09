# uses a hillclimber to cut in Best first solutions

class Hillclimber(object):
    """docstring for Hillclimber."""
    def __init__(self, algorithm, game_id, game):
        """Initiate Hillclimber"""
        self.solution = self.read_solution(f"results/{algorithm}solution{game_id}.txt")
        self.game = game

    def hillclimber(self):
        """changes solution and checks if it is a viable one"""
        solution = self.cutter()
        self.game.try_solution(solution)
        return(solution)

    def cutter(self):
        """If a car moves up and down in limited move space cut one of 'em"""
        car_id_list = []
        for move in self.solution:
            car_id = move.split()[0]
            # append car_ids to a list and check how often they are present
            car_id_list.append(car_id)
        print(car_id_list)
        mode = max(set(car_id_list), key=car_id_list.count)
        print(mode, "hdahje")
        return [1, 1]

        # for id
        # if occurs more often
        # try not doing the first move if same direction

    def read_solution(self, filename):
        """reads solution (which is a .txt) and converts it back to an array"""
        sequence = []
        with open(filename, 'r') as file:
            for text_line in file:
                sequence.append(text_line.strip())
        return sequence
