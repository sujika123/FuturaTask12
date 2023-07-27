#Count number of islands where every island is row-wise and column-wise separated

# Size of given matrix is M X N
M = 6
N = 3


# This function takes a matrix of 'X' and 'O'
# and returns the number of rectangular
# islands of 'X' where no two islands are
# row-wise or column-wise adjacent, the islands
# may be diagonally adjacent
def countIslands(mat):
    count = 0;  # Initialize result

    # Traverse the input matrix
    for i in range(0, M):

        for j in range(0, N):

            # If current cell is 'X', then check
            # whether this is top-leftmost of a
            # rectangle. If yes, then increment count
            if (mat[i][j] == 'X'):

                if ((i == 0 or mat[i - 1][j] == 'O') and
                        (j == 0 or mat[i][j - 1] == 'O')):
                    count = count + 1

    return count


# Driver Code
mat = [['O', 'O', 'O'],
       ['X', 'X', 'O'],
       ['X', 'X', 'O'],
       ['O', 'O', 'X'],
       ['O', 'O', 'X'],
       ['X', 'X', 'O']]

print("Number of rectangular islands is",
      countIslands(mat))