#Find Second largest element in an array

#Algorithm

# Input: arr[] = {12, 35, 1, 10, 34, 1}
# Output: The second largest element is 34.
# Explanation: The largest element of the
# array is 35 and the second
# largest element is 34
#
# Input: arr[] = {10, 5, 10}
# Output: The second largest element is 5.
# Explanation: The largest element of
# the array is 10 and the second
# largest element is 5
#
# Input: arr[] = {10, 10, 10}
# Output: The second largest does not exist.
# Explanation: Largest element of the array
# is 10 there is no second largest element

#Program

def print2largest(arr,
                  arr_size):
    # There should be
    # atleast two elements
    if (arr_size < 2):
        print(" Invalid Input ")
        return

    # Sort the array
    arr.sort

    # Start from second last
    # element as the largest
    # element is at last
    for i in range(arr_size - 2,
                   -1, -1):

        # If the element is not
        # equal to largest element
        if (arr[i] != arr[arr_size - 1]):
            print("The second largest element is",
                  arr[i])
            return

    print("There is no second largest element")


# Driver code
arr = [12, 35, 1, 10, 34, 1]
n = len(arr)
print2largest(arr, n)

