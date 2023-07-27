#Find the element that appears once in Array where every other element appears twice

def findSingle(A, ar_size):
    # iterate over every element
    for i in range(ar_size):

        # Initialize count to 0
        count = 0
        for j in range(ar_size):

            # Count the frequency
            # of the element
            if (A[i] == A[j]):
                count += 1

        # If the frequency of
        # the element is one
        if (count == 1):
            return A[i]

    # If no element exist
    # at most once
    return -1


ar = [2, 3, 5, 4, 5, 3, 4]
n = len(ar)
# Function call
print("Element occurring once is", findSingle(ar, n))

