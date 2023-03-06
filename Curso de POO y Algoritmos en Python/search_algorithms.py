# Algoritmos de Busqueda lineal, Sentinela y Binaria

# Linear search is the basic search that moves element from element

def linear_search(array, value):
    for i in range(0, len(array)):
        if array[i] == value:
            return True
        
    return False


# Sentinel search adds the value at the end to guarantee that it will be found

def sentinel_search(array, value):
    array.append(value)

    i = 0
    while array[i] != value:
        i += 1
    
    array.pop()
    if i < len(array):
        return True
    else:
        return False


# Binary Search requires a sorted iterable to work.

def binary_search(array, value, start, end):
    
    while start <= end:
        middle = (start + end) // 2

        if array[middle] == value:
            return True
        elif array[middle] > value:
            end = middle - 1
        else:
            start = middle + 1

    return False



if __name__ == '__main__':
    numbers_list = [5, 2, 1, 34, 21, 234, 1]
    sorted_number_list = sorted(numbers_list)

    print(linear_search(numbers_list, 35))
    print(sentinel_search(numbers_list, 35))
    print(binary_search(sorted_number_list, 234, 0, len(sorted_number_list)))