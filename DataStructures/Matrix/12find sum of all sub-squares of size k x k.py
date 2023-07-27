#Given an n x n square matrix, find sum of all sub-squares of size k x k

# Size of given matrix
n = 5


# A simple function to find sum of all
# sub-squares of size k x k in a given
# square matrix of size n x n
def printSumSimple(mat, k):
    # k must be smaller than or equal to n
    if (k > n):
        return

    # row number of first cell in current
    # sub-square of size k x k
    for i in range(n - k + 1):

        # column of first cell in current
        # sub-square of size k x k
        for j in range(n - k + 1):

            # Calculate and print sum of
            # current sub-square
            sum = 0
            for p in range(i, k + i):
                for q in range(j, k + j):
                    sum += mat[p][q]
            print(sum, end=" ")

        # Line separator for sub-squares
        # starting with next row
        print()


# Driver Code
if __name__ == "__main__":
    mat = [[1, 1, 1, 1, 1],
           [2, 2, 2, 2, 2],
           [3, 3, 3, 3, 3],
           [4, 4, 4, 4, 4],
           [5, 5, 5, 5, 5]]
    k = 3
    printSumSimple(mat, k)


