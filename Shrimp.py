import Crab


class Shrimp(Crab.Crab):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)
        self.width = 7
        self.height = 3

    def get_animal(self):
        shrimpL = [["*", " ", "*", " ", " ", " ", " "],
                   [" ", "*", "*", "*", "*", "*", "*"],
                   [" ", " ", "*", " ", "*", " ", " "]]

        shrimpR = [[" ", " ", " ", " ", "*", " ", "*"],
                   ["*", "*", "*", "*", "*", "*", " "],
                   [" ", " ", "*", " ", "*", " ", " "]]

        if self.directionH == 0:
            return shrimpL
        else:
            return shrimpR