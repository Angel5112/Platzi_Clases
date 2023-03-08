"""
Reto - Clase de Linked Lists

1. Crear una Singly Linked List
2. Crear un arreglo y meterle elementos al azar
3. Pasa todos los elementos del arreglo a la lista
"""

from random import randint

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
    
    def fill_numbers(self):
        for i in range(self.__len__()):
            value = randint(1, 20)
            self.__setitem__(i, value)


class Node:

    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LinkedList:

    def __init__(self):
        self.head = None

    def add_end(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.link != None:
                current = current.link

            current.link = node

    def print_list(self):
        current = self.head
        while current:
            print(f"{current.data}", end=' ---> ')
            current = current.link
        
        print('NULL')

    def insert_array_elements(self, array):
        for i in range(array.__len__()):
            self.add_end(array.items[i])



if __name__ == '__main__':
    size = int(input("Enter the size of the array: "))
    arr = Array(size)

    arr.fill_numbers()
    print(arr.__str__())

    lista = LinkedList()
    lista.insert_array_elements(arr)
    lista.print_list()