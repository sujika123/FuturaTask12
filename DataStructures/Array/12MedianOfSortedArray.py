#Median of two sorted arrays


def getMedian(ar1, ar2, n):
    i, j = n - 1, 0

    # while loop to swap all smaller numbers to arr1
    while (ar1[i] > ar2[j] and i > -1 and j < n):
        ar1[i], ar2[j] = ar2[j], ar1[i]
        i -= 1
        j += 1

    ar1.sort()
    ar2.sort()

    return (ar1[-1] + ar2[0]) >> 1


# Driver program
if __name__ == '__main__':
    ar1 = [1, 12, 15, 26, 38]
    ar2 = [2, 13, 17, 30, 45]

    n1, n2 = len(ar1), len(ar2)

    if (n1 == n2):
        print('Median is', getMedian(ar1, ar2, n1))
    else:
        print("Doesn't work for arrays of unequal size")
