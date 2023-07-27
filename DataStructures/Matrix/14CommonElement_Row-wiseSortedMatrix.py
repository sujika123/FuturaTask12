#Find a common element in all rows of a given row-wise sorted matrix

M = 4
N = 5


# Returns common element in all rows
# of mat[M][N]. If there is no common
# element, then -1 is returned
def findCommon(mat):
    # An array to store indexes of
    # current last column
    column = [N - 1] * M

    min_row = 0  # Initialize min_row as first row

    # Keep finding min_row in current last
    # column, till either all elements of
    # last column become same or we hit first column.
    while (column[min_row] >= 0):

        # Find minimum in current last column
        for i in range(M):
            if (mat[i][column[i]] <
                    mat[min_row][column[min_row]]):
                min_row = i

        # eq_count is count of elements equal
        # to minimum in current last column.
        eq_count = 0

        # Traverse current last column elements
        # again to update it
        for i in range(M):

            # Decrease last column index of a row
            # whose value is more than minimum.
            if (mat[i][column[i]] >
                    mat[min_row][column[min_row]]):
                if (column[i] == 0):
                    return -1

                column[i] -= 1  # Reduce last column
                # index by 1

            else:
                eq_count += 1

        # If equal count becomes M, return the value
        if (eq_count == M):
            return mat[min_row][column[min_row]]
    return -1


# Driver Code
if __name__ == "__main__":

    mat = [[1, 2, 3, 4, 5],
           [2, 4, 5, 8, 10],
           [3, 5, 7, 9, 11],
           [1, 3, 5, 7, 9]]

    result = findCommon(mat)
    if (result == -1):
        print("No common element")
    else:
        print("Common element is", result)