from copy import deepcopy


class Iterative(object):
    """docstring for Iterative."""
    def __init__(self, car_list, final_car_list, game):
        """Initialization method."""
        self.game = game
        self.final_car_list = final_car_list
        self.inital_car_list = car_list
        self.thing = self.iterative()

    def update_car_list(self, car_list):
        self.current_car_list = car_list

    def compare_value(self):
        """Compares the dict made in assign_value() with the final dict.
        If the values match give a possitive value to the value_dict"""
        self.board_value = 0
        self.update_car_list(self.game.car_list)
        final_dict = self.compare_i_f()
        comparison_dict = self.assign_value()
        keys = list(comparison_dict.keys())
        for key in keys:
            if comparison_dict[key] == final_dict[key[0]]:
                # increase the value
                self.board_value += 1
            else:
                # decrease the value
                self.board_value -= 1
        # move = max(self.value_dict, key=self.value_dict.get)
        # do the move
        print(self.board_value)
        # self.game.move(list(move[1]), move[0], self.current_car_list)


    def assign_value(self):
        """Retrieves finalized board"""
        # find possible moves
        command_list = self.game.make_possible_move()
        comparison_dict = {}
        for move in command_list:
            car = self.current_car_list[int(move[0]) - 1]
            # compare moves with cars final state
            if car.direction == "x":
                diffence = car.coordinate[0][0] - move[1][0]
                move_m = tuple(move[1])
                move = (move[0], move_m)
                if diffence > 0:
                    comparison_dict[move] = "-"
                elif diffence < 0:
                    comparison_dict[move] = "+"
                else:
                    comparison_dict[move] = "0"
            else:
                diffence = car.coordinate[0][1] - move[1][1]
                move_m = tuple(move[1])
                move = (move[0], move_m)
                if diffence > 0:
                    comparison_dict[move] = "-"
                elif diffence < 0:
                    comparison_dict[move] = "+"
                else:
                    comparison_dict[move] = "0"
        return comparison_dict

    def compare_i_f(self):
        """Calculates the difference between xi and xf"""
        final_dict = {}
        if self.final_car_list:
            for car in self.inital_car_list:
                if car.direction == "x":
                    diffence = car.coordinate[0][0] - self.final_car_list[int(car.id) - 1].coordinate[0][0]
                    if diffence > 0:
                        final_dict[car.id] = "-"
                    elif diffence < 0:
                        final_dict[car.id] = "+"
                    else:
                        final_dict[car.id] = "0"
                else:
                    diffence = car.coordinate[0][1] - self.final_car_list[int(car.id) - 1].coordinate[0][1]
                    if diffence > 0:
                        final_dict[car.id] = "-"
                    elif diffence < 0:
                        final_dict[car.id] = "+"
                    else:
                        final_dict[car.id] = "0"
        return final_dict

    def iterative(self):
        while not self.game.won():
            self.compare_value()
            break
        pass
