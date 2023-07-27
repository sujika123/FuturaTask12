#Inplace M x N size matrix transpose | Updated

HASH_SIZE = 128


#  A utility function to pr a 2D array
#  of size nr x nc and base address A
def Pr2DArray(A, nr, nc):
    for r in range(nr):
        for c in range(nc):
            print('{0: >4}'.format(str(A[r * nc + c])), end="")
        print()
    print()


#  Non-square matrix transpose of
#  matrix of size r x c and base address A
def MatrixInplaceTranspose(A, r, c):
    size = r * c - 1

    b = 1;  # hash to mark moved elements

    b |= (1 << size)

    i = 1;  # Note that A[0] and A[size-1] won't move
    while (i < size):

        cycleBegin = i
        t = A[i];
        while True:

            #  Input matrix [r x c]
            #  Output matrix
            #  i_new = (i*r)%(N-1)
            next1 = (i * r) % size
            temp = A[next1]
            A[next1] = t
            t = temp
            b |= (1 << i)
            i = next1;
            if i == cycleBegin:
                break

        #  Get next1 Move (what about querying random location?)
        i = 1
        while i < size and ((b & (1 << i)) != 0):
            i += 1

        print()
    return A


#  Driver program to test above function
r = 5
c = 6
size = r * c
A = [i + 1 for i in range(size)]

Pr2DArray(A, r, c)
A = MatrixInplaceTranspose(A, r, c)
Pr2DArray(A, c, r)
