#Usando Heranças

class Animal:
    def __init__(self, age: int, height: int, weight: int, position: tuple):
        self.age = age
        self.height = height
        self.weight = weight
        self.position: tuple = position

    def move_x(self):
        self.position[0] += 1

    def move_y(self):
        self.position[1] += 1

    def move_z(self):
        self.position[2] += 1


class Dog(Animal):
    def __init__(self, age: int, height: int, weight: int, position: tuple):
        Animal.__init__(self, age, height, weight, position)

    def move_z(self):
        self.position[2] += 2


caramelo = Dog(10, 9, 9, (0, 0, 0))
print(caramelo.height)