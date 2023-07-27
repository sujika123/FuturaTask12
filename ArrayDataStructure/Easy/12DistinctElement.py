#Print All Distinct Elements of a given integer array

def printDistinct(arr, n):
    # Pick all elements one by one
    for i in range(0, n):

        # Check if the picked element
        # is already printed
        d = 0
        for j in range(0, i):
            if (arr[i] == arr[j]):
                d = 1
                break

        # If not printed earlier,
        # then print it
        if (d == 0):
            print(arr[i])


# Driver program to test above function
arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]
n = len(arr)
printDistinct(arr, n)

