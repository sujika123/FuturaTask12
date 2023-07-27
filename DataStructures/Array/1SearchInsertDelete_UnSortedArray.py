#Search, insert and delete in an unsorted array

# Python program for searching in
# unsorted array

print("\nSearch Operation:")
def findElement(arr, n, key):
    for i in range(n):
        if (arr[i] == key):
            return i

    # If the key is not found
    return -1


# Driver's code
if __name__ == '__main__':
    arr = [12, 34, 10, 6, 40]
    key = 40
    n = len(arr)

    # search operation
    index = findElement(arr, n, key)
    if index != -1:
        print("Element Found at position: " + str(index + 1))
    else:
        print("Element not found")


print("___________________________________________")
print()
print("Insert Operation:")
print()
print("1. Insert at the end:")


# Python program for inserting
# an element in an unsorted array

# method to insert element


def insert(arr, element):
    arr.append(element)


# Driver's code
if __name__ == '__main__':
    # declaring array and key to insert
    arr = [12, 16, 20, 40, 50, 70]
    key = 26

    # array before inserting an element
    print("Before Inserting: ")
    print(arr)

    # array after Inserting element
    insert(arr, key)
    print("After Inserting: ")
    print(arr)

print()
print("2. Insert at any position")


# python Program to Insert an element
# at a specific position in an Array
def insertElement(arr, n, x, pos):
    # shift elements to the right
    # which are on the right side of pos
    for i in range(n - 1, pos - 1, -1):
        arr[i + 1] = arr[i]

    arr[pos] = x


# Driver's code
if __name__ == '__main__':
    # Declaring array and key to delete
    # here -1 is for empty space
    arr = [2, 4, 1, 8, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    n = 5

    print("Before insertion : ")
    for i in range(0, n):
        print(arr[i], end=' ')

    print("\n")

    x = 10;
    pos = 2;

    # Function call
    insertElement(arr, n, x, pos);
    n += 1

    print("After insertion : ")
    for i in range(0, n):
        print(arr[i], end=' ')
print()
print("___________________________________________________")
print("\nDelete Operation:\n")

# Python program to delete an element
# from an unsorted array

# Driver's code
if __name__ == '__main__':
    # Declaring array and key to delete
    arr = [10, 50, 30, 40, 20]
    key = 30

    print("Array before deletion:")
    print(arr)

    # deletes key if found in the array
    # otherwise shows error not in list
    arr.remove(key)
    print("Array after deletion")
    print(arr)