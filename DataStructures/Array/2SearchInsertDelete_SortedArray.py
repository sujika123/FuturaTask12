#Search, Insert, and Delete in an Sorted Array

print("\nSearch Operation:")

# python 3  program to implement
# binary search in sorted array

def binarySearch(arr, low, high, key):
    mid = (low + high) / 2

    if (key == arr[int(mid)]):
        return mid

    if (key > arr[int(mid)]):
        return binarySearch(arr,
                            (mid + 1), high, key)

    if (key < arr[int(mid)]):
        return binarySearch(arr, low, (mid - 1), key)

    return 0


# Driver code
if __name__ == "__main__":
    # Let us search 3 in below array
    arr = [5, 6, 7, 8, 9, 10]
    n = len(arr)
    key = 10

    # Function call
    print("Index:", int(binarySearch(arr, 0, n - 1, key)))

print("___________________________________________________")

print("Insert Operation:")
# Python3 program to implement insert
# operation in an sorted array.

# Inserts a key in arr[] of given capacity.
# n is current size of arr[]. This function
# returns n+1 if insertion is successful, else n.


def insertSorted(arr, n, key, capacity):
    # Cannot insert more elements if n is
    # already more than or equal to capacity
    if (n >= capacity):
        return n

    i = n - 1
    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]
        i -= 1

    arr[i + 1] = key

    return (n + 1)


# Driver Code
if __name__ == "__main__":
    arr = [12, 16, 20, 40, 50, 70]

    for i in range(20):
        arr.append(0)

    capacity = len(arr)
    n = 6
    key = 26

    print("Before Insertion: ", end=" ")
    for i in range(n):
        print(arr[i], end=" ")

    # Function call
    n = insertSorted(arr, n, key, capacity)

    print("\nAfter Insertion: ", end="")
    for i in range(n):
        print(arr[i], end=" ")

print("\n_________________________________________________")

print("\nDelete Operation:\n")

# Python program to implement delete operation in a
# sorted array

# /* Function to delete an element */


def deleteElement(arr, n, key):
    # Find position of element to be deleted
    pos = binarySearch(arr, 0, n - 1, key)

    if (pos == -1):
        print("Element not found")
        return n

    # Deleting element
    for i in range(pos, n - 1):
        arr[i] = arr[i + 1]

    return n - 1


# To search a key to be deleted


def binarySearch(arr, low, high, key):
    if (high < low):
        return -1
    mid = (low + high) // 2

    if (key == arr[mid]):
        return mid
    if (key > arr[mid]):
        return binarySearch(arr, (mid + 1), high, key)

    return binarySearch(arr, low, (mid - 1), key)


# Driver code
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]

    n = len(arr)
    key = 30

    print("Array before deletion")

    for i in range(n):
        print(arr[i], end=" ")

    # Function call
    n = deleteElement(arr, n, key)
    print("\n\nArray after deletion")
    for i in range(n):
        print(arr[i], end=" ")
