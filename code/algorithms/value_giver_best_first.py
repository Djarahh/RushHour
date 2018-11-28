class ValueGiver(object):
    """docstring for Iterative."""
    def __init__(self, car_list, final_car_list, game):
        """Initialization method."""
        self.game = game
        self.final_car_list = final_car_list
        self.inital_car_list = car_list

    def value_giver(self):
        """Calculates the difference between xi and xf"""
        self.board_value = 0
        if self.final_car_list:
            for car in self.inital_car_list:
                if car.direction == "x":
                    difference = abs(car.coordinate[0][0] - self.final_car_list[int(car.id) - 1].coordinate[0][0])
                    self.board_value += difference
                else:
                    difference = abs(car.coordinate[0][1] - self.final_car_list[int(car.id) - 1].coordinate[0][1])
                    self.board_value += difference
        print(self.board_value)
