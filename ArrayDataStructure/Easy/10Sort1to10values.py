#Sort an array which contain 1 to n values


def sort(arr, n):
    i = 0
    while (i < n):
        # finding the corrent index
        correct = arr[i] - 1

        # Element index and value not match
        # then swapping
        if arr[correct] != arr[i]:
            # calling swap function
            swap(arr, i, correct)
        else:
            i = i + 1


# function to swap values
def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp


# Driver Code
arr = [3, 2, 5, 6, 1, 4]
n = len(arr)

# function call
sort(arr, n)

# printing the answer
for i in range(0, n):
    print(arr[i], end=" ")
