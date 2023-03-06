# Bubble, Insertion and QuickSort Algorithms

# Bubble sort

def bubble_sort(array, size):

    for i in range(0, size):
        for j in range(0, size - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]



# Insertion sort

def insertion_sort(array, size):

    for i in range(1, size):
        t = array[i]
        j = i
        while j > 0 and t < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1

        array[j] = t


# Function to work with pivots

def partition(list, low, high):
    i = low
    pivot = list[high]

    for j in range(low, high):
        if list[j] <= pivot:
            list[i], list[j] =  list[j], list[i]
            i += 1

    list[i], list[high] = list[high] ,list[i]

    return i

# Quicksort

def quick_sort(list, low, high):
    if low < high:
        partition_index = partition(list, low, high)
        quick_sort(list, low, partition_index - 1)
        quick_sort(list, partition_index + 1, high)


if __name__ == '__main__':
    array1 = [4, 2, 1, 45, 21, 10]
    array2 = [6, 11, 223, 1, 2, 4, 3]
    array3 = [76, 12, 1, 45, 32, 4, 12]

    bubble_sort(array1, len(array1))
    insertion_sort(array2, len(array2))
    quick_sort(array3, 0, len(array3) - 1)

    print(array1)
    print(array2)
    print(array3)