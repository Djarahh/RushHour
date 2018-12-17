from code.classes.car import Car


class LoadSolution(object):
    """
    Creates a string containing the cars for the initialization of the
    game. Requires a txt file of the cars
    """
    def __init__(self, game):
        """
        Initialization of LoadCars object

        game = string, only a single number
        """
        self.car_list = self.load_solution(f"data/solutioncars{game}.txt")

    def load_solution(self, filename):
        """
        Loads the cars into rushhour

        filename = string
        """
        car_list = []
        with open(filename, 'r') as file:
            for text_line in file:
                text_line = text_line.strip()
                if text_line.isdigit():
                    id = int(text_line)
                elif text_line.startswith("length"):
                    length = int(text_line.rsplit()[1])
                elif text_line.startswith("color"):
                    color = text_line.rsplit()[1]
                elif text_line.startswith("location"):
                    coordinate_list = self.make_car_coordinate_list(file)
                    car = Car(id, length, color, coordinate_list)
                    car_list.append(car)
        return car_list

    def make_car_coordinate_list(self, file):
        """
        Makes list of coordinates of the car

        file = file
        """
        coordinate_list = []
        while True:
            coordinate = file.readline().strip().split(",")
            if coordinate[0] is not "":
                row = int(coordinate[0])
                column = int(coordinate[1])
                coordinate_list.append([row, column])
            else:
                break
        return coordinate_list
