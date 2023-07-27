#Square Root (Sqrt) Decomposition Algorithm

arr = [0] * 10000  # original array


# Time Complexity: O(r-l+1)
def query(l, r):
    _sum = 0
    for i in range(l, r + 1):
        _sum += arr[i]
    return _sum


# Driver code
if __name__ == '__main__':
    # We have used separate list for input because
    # the purpose of this code is to explain simple
    # array query using iteration in competitive
    # programming where we have multiple inputs.
    input_arr = [1, 5, 2, 4, 6, 1, 3, 5, 7, 10]

    # copying input_arr to arr
    arr[:len(input_arr)] = input_arr

    print("query(3,8) :", query(3, 8))
    print("query(1,6) :", query(1, 6))
    arr[8] = 0  # updating arr[8] to 0
    print("query(8,8) :", query(8, 8))