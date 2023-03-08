# Simple Operations in Linked Lists (The rest are in the Data Structures Repository)

class Node:

    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LinkedList:

    def __init__(self):
        self.head = None

    # Insert at the end

    def insert_end(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.link != None:
                current = current.link

            current.link = new_node

    # Insert at the start

    def insert_start(self, data):
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            self.head = new_node
            self.head.link = current

    # Print the list

    def print_list(self):
        current = self.head
        while current:
            print(f"{current.data}", end=' ---> ')
            current = current.link

        print('NULL')

    # Delete node at the end

    def delete_end(self):
        if self.head == None:
            print("The list is already empty!")
        else:
            current = self.head
            while current.link.link:
                current = current.link
            
            current.link = None

    # Delete node at the beginning

    def delete_start(self):
        if self.head == None:
            print("The list is already empty!")
        else:
            current = self.head
            self.head = current.link
            current = None

    # Search for an element

    def search(self, value):
        current = self.head

        while current:
            if current.data == value:
                return True
            
            current = current.link

        return False
    
    # Returns the lenght of the list

    def __len__(self):
        current = self.head
        size = 0

        while current:
            size += 1
            current = current.link

        return size
    
    # Remove all nodes of the list

    def clear(self):
        self.head = None


if __name__ == '__main__':
    lista = LinkedList()

    num_nodes = int(input("Enter the number of nodes: "))

    for i in range(num_nodes):
        value = int(input(f"Enter the value of the node {i}: "))
        lista.insert_end(value)

    lista.print_list()

    value = int(input("Enter the value of the node that will be inserted at the beginning: "))
    lista.insert_start(value)

    value = int(input("Enter the value of the node that will be inserted at the beginning: "))
    lista.insert_end(value)

    lista.print_list()

    print("\nThe last node will be deleted!")
    lista.delete_end()
    lista.print_list()

    print("\nThe first node will be deleted!")
    lista.delete_start()
    lista.print_list()

    value = int(input("Enter the value to search on the list: "))
    print(f"Is {lista.search(value)} that the value {value} is on the list!")

    print(f"The size of the list is: {lista.__len__()}")
    print("\nThe list will be cleaned!")
    lista.clear()
    lista.print_list()
