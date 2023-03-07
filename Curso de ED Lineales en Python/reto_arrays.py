"""
Reto - Clase de Arrays

1. Crea una clase Array
2. Incorpora un metodo para poblar sus slots con numeros aleatorios
3. Incluye un metodo que sume todos los valores del array
"""

import random

class Array:

    def __init__(self, size, fill_value=None):
        self.items = list()

        for i in range(size):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __setitem__(self, index, value):
        self.items[index] = value
        
    def __getitem__(self, index):
        return self.items[index]
    
    def __rand_numbers__(self):
        for i in range(self.__len__()):
            value = random.randint(1, 11)
            arr.__setitem__(i, value)

    def __sum__(self):
        sum = 0
        for i in range(self.__len__()):
            num = self.__getitem__(i)
            sum += num

        return sum



if __name__ == '__main__':
    length = int(input("Enter the size of the array: "))
    arr = Array(length)

    arr.__rand_numbers__()
    print(arr.__str__())
    print(arr.__sum__())