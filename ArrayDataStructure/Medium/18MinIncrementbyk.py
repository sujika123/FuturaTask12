#Minimum increment by k operations to make all elements equal

def minOps(arr, n, k):
    # max elements of array
    max1 = max(arr)
    res = 0

    # iterate for all elements
    for i in range(0, n):

        # check if element can make equal to
        # max or not if not then return -1
        if ((max1 - arr[i]) % k != 0):
            return -1

        # else update res for
        # required operations
        else:
            res += (max1 - arr[i]) / k

    # return result
    return int(res)


# driver program
arr = [21, 33, 9, 45, 63]
n = len(arr)
k = 6
print(minOps(arr, n, k))


