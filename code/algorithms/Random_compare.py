from code.algorithms.random_possible_moves import Randomize
from copy import deepcopy


class Find_pattern(object):
    def __init__(self, game, solution):
        self.game = game
        self.solution = solution

    def make_solutions(self, x):
        solutions = []
        for i in range(x):
            random = Randomize(deepcopy(self.game))
            solution = random.randomize()
            solutions.append(solution)
        return solutions

    def find_pattern(self, x):
        solutions = self.make_solutions(x)
        for solution in solutions:
            self.compare(solution)

    def compare(self, solution):
        print(f"Length: {len(solution)}")
        for i in range(len(solution)):
            if solution[i][0] == 2 and solution[i][1] == [3,4,5]:
                print("yay")
                print(i)
                print(solution[i])
                set = i
                for i in range(set, len(solution)):
                    if solution[i][0] == 3 and not solution[i][1] != [3,4]:
                        print("woopdiedoo")
                        print(i)
                        print(solution[i])
                        set = i
                        break

        # for i in range(len(self.solution)- 2):
        #     for j in range(len(solution)- 1):
        #         if self.solution[i] == solution[j] and self.solution[i + 1] == solution[j + 1]:
        #             print(f"Moves(bfs): {self.solution[i]} and {self.solution[i+1]}")
        #             for k in range(len(solution) - j - 1):
        #                 if self.solution[i + 2] == solution[j + k]:
        #                     print(k)
        #                     print(self.solution[i + 2])
        #                     break
        # for i in range(len(solution)):
        #     if solution[i][0] == 7 and solution[i][1] in [[0,1], [3,4], [4,5]]:
        #         print("yay")
        #     if solution[i][0] == 6 and solution[i][1] == [3,4,5]:
        #         print("woop")
        #         print(i)
