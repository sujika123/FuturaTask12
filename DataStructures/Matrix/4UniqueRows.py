#Print unique rows in a given boolean matrix

ROW = 4
COL = 5


# The main function that prints
# all unique rows in a given matrix.
def findUniqueRows(M):
    # Traverse through the matrix
    for i in range(ROW):
        flag = 0

        # Check if there is similar column
        # is already printed, i.e if i and
        # jth column match.
        for j in range(i):
            flag = 1

            for k in range(COL):
                if (M[i][k] != M[j][k]):
                    flag = 0

            if (flag == 1):
                break

        # If no row is similar
        if (flag == 0):

            # Print the row
            for j in range(COL):
                print(M[i][j], end=" ")

            print()

        # Driver Code


if __name__ == '__main__':
    M = [[0, 1, 0, 0, 1],
         [1, 0, 1, 1, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 1, 0, 0]]

    findUniqueRows(M)
