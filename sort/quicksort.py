def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            (array[i + 1], array[j]) = (array[j], array[i + 1])
            i = i + 1
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def qs(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        qs(array, pivot + 1, high)
        qs(array, low, pivot - 1)


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

qs(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
