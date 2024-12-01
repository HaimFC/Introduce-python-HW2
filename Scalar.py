import Fish


class Scalar(Fish.Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name, age, x, y, directionH, directionV)
        self.width = 8
        self.height = 5

    def get_animal(self):
        scalarR = [["*", "*", "*", "*", "*", "*", " ", " "],
                   [" ", " ", " ", " ", "*", "*", "*", " "],
                   [" ", " ", "*", "*", "*", "*", "*", "*"],
                   [" ", " ", " ", " ", "*", "*", "*", " "],
                   ["*", "*", "*", "*", "*", "*", " ", " "]]

        scalarL = [[" ", " ", "*", "*", "*", "*", "*", "*"],
                   [" ", "*", "*", "*", " ", " ", " ", " "],
                   ["*", "*", "*", "*", "*", "*", " ", " "],
                   [" ", "*", "*", "*", " ", " ", " ", " "],
                   [" ", " ", "*", "*", "*", "*", "*", "*"]]

        if self.directionH == 0:
            return scalarL
        else:
            return scalarR