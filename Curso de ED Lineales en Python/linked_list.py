"""
Linked list = Estructura de datos lineal en forma de recorrido. Junta un conjunto de nodos, cada uno con un elemento y el enlance al siguiente nodo
"""

class Node:

    # Creacion de un Nodo

    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LinkedList:

    # Creacion de una Lista Simplemente Enlazada

    def __init__(self):
        self.head = None
        self.size = 0

    # Agregar elemento al final de la lista

    def add_end(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
            self.size += 1
        else:
            current = self.head
            while current.link != None:
                current = current.link

            current.link = node
            self.size += 1

    # Imprimir la lista simplemente enlazada

    def print_list(self):
        current = self.head
        while current:
            print(f"{current.data}", end=' ---> ')
            current = current.link

        print("NULL")

    # Mostrar el size de la lista

    def __len__(self):
        return self.size        # Si se tiene implementado con size, sino, tocara usar un while y un contador elemento por elemento
    
    # Buscar un elemento en la lista

    def search(self, value):
        current = self.head

        while current:
            if current.data == value:
                return True
            
            current = current.link

        return False
    
    # Eliminar la lista
    
    def clear(self):
        self.head = None
        self.size = 0



if __name__ == '__main__':
    lista = LinkedList()

    node_num = int(input("Enter the number of nodes: "))
    
    for i in range(node_num):
        value = int(input(f"Enter the value of the node {i}: "))
        lista.add_end(value)

    lista.print_list()
    print(f"The size of the list is: {lista.__len__()}")
    
    search_value = int(input("Enter the value to search: "))
    print(f"Is {lista.search(search_value)} that the element {search_value} is on the list")
    lista.clear()
    lista.print_list()