import Animal
import Fish
import Crab
import Shrimp
import Scalar
import Moly
import Ocypode

MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7
MAX_FISH_HEIGHT = 5
MAX_FISH_WIDTH = 8
WATERLINE = 3
FEED_AMOUNT = 10
MAX_AGE = 120


class Aqua:
    def __init__(self, aqua_width, aqua_height):
        self.turn = 0
        self.aqua_height = aqua_height
        self.aqua_width = aqua_width
        self.board = [' '] * self.aqua_height
        self.build_tank(aqua_height, aqua_width)
        self.anim = []

    def build_tank(self, aqua_height, aqua_width):
        aqua_tank_w = []
        for y in range(0, aqua_height):
            if y == 2:
                for x in range(0, aqua_width):
                    if x == 0 or x == aqua_width - 1:
                        aqua_tank_w.append('|')
                    else:
                        aqua_tank_w.append('~')
                self.board[2] = aqua_tank_w.copy()
                aqua_tank_w.clear()
            elif y == aqua_height - 1:
                for x in range(0, aqua_width):
                    if x == 0:
                        aqua_tank_w.append("\\")
                    elif x == aqua_width - 1:
                        aqua_tank_w.append('/')
                    else:
                        aqua_tank_w.append('_')
                self.board[aqua_height - 1] = aqua_tank_w.copy()
                aqua_tank_w.clear()
            else:
                for x in range(0, aqua_width):
                    if x == 0 or x == aqua_width - 1:
                        aqua_tank_w.append('|')
                    else:
                        aqua_tank_w.append(' ')
                self.board[y] = aqua_tank_w.copy()
                aqua_tank_w.clear()

    def print_board(self):
        for x in self.board:
            print(*x)

    def get_board(self):
        return self.board

    def get_all_animal(self):
        return self.anim

    def is_collision(self, animal):
        crabs = []
        for i in self.anim:
            if animal.directionH == 0:
                if i.width == 7 and i.get_alive() and i.directionH == 1:
                    if animal.x - 1 == i.x + 6 + 1:
                        crabs.append(i)
                    elif i.x + 6 <= animal.x - 1 <= i.x:
                        crabs.append(i)
            else:
                if i.width == 7 and i.get_alive() and i.directionH == 0:
                    if animal.x + 6 == i.x - 1:
                        crabs.append(i)
                    elif animal.x + 6 <= i.x - 1 <= animal.x:
                        crabs.append(i)
        if len(crabs) != 0:
            for crab in crabs:
                if crab.directionH == 1:
                    crab.directionH = 0
                    return True
                else:
                    crab.directionH = 1
                    return True
        else:
            return False

    def print_animal_on_board(self, animal: Animal):
        animalTemplate = []
        if animal.width == 8 and animal.height == 5:
            animalTemplate = Scalar.Scalar.get_animal(animal)
        elif animal.width == 8 and animal.height == 3:
            animalTemplate = Moly.Moly.get_animal(animal)
        elif animal.width == 7 and animal.height == 4:
            animalTemplate = Ocypode.Ocypode.get_animal(animal)
        else:
            animalTemplate = Shrimp.Shrimp.get_animal(animal)

        if len(animalTemplate) != 0:
            tempY = -1
            for y in range(animal.y, animal.y + animal.height):
                tempY += 1
                tempX = -1
                for x in range(animal.x, animal.x + animal.width):
                    tempX += 1
                    self.board[y][x] = animalTemplate[tempY][tempX]

    def delete_animal_from_board(self, animal: Animal):
        for y in range(animal.y, animal.y + animal.height):
            for x in range(animal.x, animal.x + animal.width):
                self.board[y][x] = " "

    def add_fish(self, name, age, x, y, directionH, directionV, fishType):
        try:
            animal1 = Fish.Fish(name, age, x, y, directionH, directionV)
            animal1.width = 8
            if x + 8 >= self.aqua_width:
                x = self.aqua_width - 9
            if x <= 0:
                x = 1
            if y <= 2:
                y = 3
            if fishType == "sc":
                animal1.height = 5
                if y >= self.aqua_height - 9:
                    y = self.aqua_height - 10
            elif fishType == "mo":
                animal1.height = 3
                if y >= self.aqua_height - 7:
                    y = self.aqua_height - 8
            check = self.check_if_free(x, y)
            animal1.x, animal1.y = x, y
            if check:
                if fishType == "sc":
                    an = Scalar.Scalar(name, age, x, y, directionH, directionV)
                    self.anim.append(an)
                    self.print_animal_on_board(animal1)
                elif fishType == "mo":
                    an = Moly.Moly(name, age, x, y, directionH, directionV)
                    self.anim.append(an)
                    self.print_animal_on_board(animal1)
                return True
            else:
                return False
        except:
            return False

    def add_crab(self, name, age, x, y, directionH, crabType):
            animal1 = Crab.Crab(name, age, x, y, directionH)
            animal1.width = 7
            if x + 7 >= self.aqua_width:
                x = self.aqua_width - 8
            if x <= 0:
                x = 1
            y = self.aqua_height - 5 if crabType == 'oc' else self.aqua_height - 4

            check = self.check_if_free(x, y)
            animal1.x, animal1.y = x, y
            if check:
                if crabType == "oc":
                    animal1.height = 4
                    an = Ocypode.Ocypode(name, age, x, y, directionH)
                    self.anim.append(an)
                    self.print_animal_on_board(animal1)
                elif crabType == "sh":
                    animal1.height = 3
                    an = Shrimp.Shrimp(name, age, x, y, directionH)
                    self.anim.append(an)
                    self.print_animal_on_board(animal1)

                return True
            else:
                return False

    def check_if_free(self, x, y) -> bool:
        counter = 0
        if y != (self.aqua_height - 5) and y != (self.aqua_height - 4):
            yCount = -1
            for m in self.board:
                yCount += 1
                for n in range(x, x + MAX_FISH_WIDTH):
                    if y <= yCount < (y + MAX_FISH_HEIGHT):
                        if m[n] == " ":
                            counter += 1
            if counter == MAX_FISH_HEIGHT * MAX_FISH_WIDTH:
                return True
            else:
                print("The place is not available! Please try again later.")
                return False
        else:
            crabAreaY = 5
            while crabAreaY != 0:
                for n in range(x, x + MAX_CRAB_WIDTH):
                    if self.board[self.aqua_height - crabAreaY][n] == " ":
                        counter += 1
                crabAreaY -= 1
            if counter == MAX_CRAB_HEIGHT * MAX_CRAB_WIDTH:
                return True
            else:
                print("The place is not available! Please try again later.")
                return False

    def left(self, a):
        self.delete_animal_from_board(a)
        a.x -= 1
        self.print_animal_on_board(a)

    def right(self, a):
        self.delete_animal_from_board(a)
        a.x += 1
        self.print_animal_on_board(a)

    def up(self, a):
        self.delete_animal_from_board(a)
        a.y -= 1
        self.print_animal_on_board(a)

    def down(self, a):
        self.delete_animal_from_board(a)
        a.y += 1
        self.print_animal_on_board(a)

    def next_turn(self):
        # Check life and food before movement
        if self.turn % 10 == 0:
            for i in self.anim:
                i.dec_food()
        if self.turn % 100 == 0 and self.turn != 0:
            for i in self.anim:
                i.inc_age()
        for i in self.anim:
            if i.get_alive():
                if i.get_food_amount() == 0:
                    self.delete_animal_from_board(i)
                    i.starvation()
                if i.get_age() == 120:
                    self.delete_animal_from_board(i)
                    i.die()

        # Take care of the crabs collision
        crabs = []
        for i in self.anim:
            if i.width == 7 and self.is_collision(i):
                if i.directionH == 1:
                    i.directionH = 0
                else:
                    i.directionH = 1

        # Move all the fish to the correct direction (with borders)
        for animal in self.anim:
            if animal.get_alive():
                sumBorders = self.check_Borders(animal)
                if len(sumBorders) != 0:
                    for border in sumBorders:
                        if border == "right":
                            self.delete_animal_from_board(animal)
                            animal.directionH = 0
                            self.print_animal_on_board(animal)
                        elif border == "left":
                            self.delete_animal_from_board(animal)
                            animal.directionH = 1
                            self.print_animal_on_board(animal)
                        elif border == "up":
                            self.delete_animal_from_board(animal)
                            animal.directionV = 0
                            self.print_animal_on_board(animal)
                        elif border == "down":
                            self.delete_animal_from_board(animal)
                            animal.directionV = 1
                            self.print_animal_on_board(animal)
                else:
                    if animal.directionH == 1:
                        self.right(animal)
                    else:
                        self.left(animal)
                    if animal.width == 8:
                        if animal.directionV == 1:
                            self.up(animal)
                        else:
                            self.down(animal)
        self.turn += 1

    def print_all(self):
        for i in self.anim:
            if i.get_alive():
                print(i)

    def feed_all(self):
        for i in self.anim:
            if i.get_alive():
                i.food += 10

    def add_animal(self, name, age, x, y, directionH, directionV, animalType):
        if animalType == 'sc' or animalType == 'mo':
            return self.add_fish(name, age, x, y, directionH, directionV, animalType)
        elif animalType == 'oc' or animalType == 'sh':
            return self.add_crab(name, age, x, y, directionH, animalType)
        else:
            return False

    def several_steps(self) -> None:
        choice = -1
        while not choice >= 0:
            try:
                choice = int(input("How many steps do you want to take?"))
            except ValueError:
                choice = -1
        for i in range(0, choice):
            self.next_turn()

    def check_Borders(self, a):
        sumBorders = []
        if a.x + a.width == self.aqua_width - 1 and a.directionH == 1:
            sumBorders.append("right")
        elif a.x - 1 == 0 and a.directionH == 0:
            sumBorders.append("left")
        if a.width == 8:
            if a.y - 1 == 2 and a.directionV == 1:
                sumBorders.append("up")
            elif a.y + a.height == self.aqua_height - 5 and a.directionV == 0:
                sumBorders.append("down")
        return sumBorders