# Criando classes e objetos no python

class Dog:
    family = "Canidae"
    def __init__(self, age: int, peso: int):
        self._age = age
        self._peso = peso


rex = Dog (10, 9)
print(f'A idade do Rex é: {rex._age} e seu peso é: {rex._peso}')

caramelo = Dog(5, 3)
print(f'A idade do Caramelo é: {caramelo._age} e seu peso é: {caramelo._peso}')

print(f'O Rex pertence ao objeto {rex.__class__.__name__}')

