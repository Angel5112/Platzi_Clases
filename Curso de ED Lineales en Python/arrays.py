# Arrays = Coleccion de datos lineales que son guardados en secuencia en la memoria

class Array:

    # Constructor of the class

    def __init__(self, size, fill_value=None):
        self.items = list()
        for i in range(size):           # We fill the whole array with None to keep a defined structure
            self.items.append(fill_value)

    # Method to find the length of the array

    def __len__(self):
        return len(self.items)
    
    # Method to return the collection as an string representation

    def __str__(self):
        return str(self.items)
    
    # Method to return an iterable of the collection
    
    def __iter__(self):
        return iter(self.items)
    
    # Method to get an item of the collection given an index
    
    def __getitem__(self, index):
        return self.items[index]
    
    # Method to change the value of an index given its new value
    
    def __setitem__(self, index, value):
        self.items[index] = value



if __name__ == '__main__':
    arr = Array(5)      # Defining an array of 5 elements

    for i in range(arr.__len__()):      # Filling the arr with the desired elements
        new_value = int(input(f"Enter the new value for the index {i}: "))
        arr.__setitem__(i, new_value)

    print(arr.__str__())   # Print the string representation of the array
    index = int(input("Give the index of an element: "))
    print(arr.__getitem__(index))