#Sort a nearly sorted (or K sorted) array

def sortNearlySortedArray(A, size, k):
    for i in range(1, size):
        key = A[i]
        j = i - 1

        # Check if the previous element is greater than the current
        # element, and shift elements to the right until the correct
        # position is found, but only if the current element is more
        # than k positions away from its correct position
        while j >= max(0, i - k) and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

    for i in range(size):
        print(A[i], end=' ')

    print()


# Driver Code
A = [2, 6, 3, 12, 56, 8]
size = 6
k = 3
sortNearlySortedArray(A, size, k)