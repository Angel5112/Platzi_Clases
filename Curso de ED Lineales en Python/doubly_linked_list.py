# Doubly Linked Lists: The nodes have references to the previous and next node

class Node:

    def __init__(self, data, link=None, prev=None):
        self.link = link
        self.data = data
        self.prev = prev


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # Add an element at the end

    def insert_end(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            prev = None
            current = self.head
            
            while current.link != None:
                current = current.link

            current.link = new_node
            new_node.prev = current
            self.tail = new_node


    # Print the list (Left to Right)

    def print_list(self):
        current = self.head

        print('NULL', end=' <--> ')
        while current:
            print(f"{current.data}", end=' <--> ')
            current = current.link

        print("NULL")

    # Print the list (Right to Left)

    def print_right(self):
        current = self.tail

        print('NULL', end=' <--> ')
        while current:
            print(f"{current.data}", end=' <--> ')
            current = current.prev

        print('NULL')

    # Size of the list

    def __len__(self):
        current = self.head
        size = 0

        while current:
            size += 1
            current = current.link

        return size
    
    # Clear the list

    def clear(self):
        self.head = None
        self.tail = None



if __name__ == '__main__':

    lista = DoublyLinkedList()

    num_nodes = int(input("Enter the number of nodes: "))
    for i in range(num_nodes):
        value = int(input(f"Enter the value of the node {i}: "))
        lista.insert_end(value)
    
    lista.print_list()
    lista.print_right()

    size = lista.__len__()
    print(f"The length of the list is: {size}")

    print(f"Clearing the list!")
    lista.clear()
    lista.print_list()