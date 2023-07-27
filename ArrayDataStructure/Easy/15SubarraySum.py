#Find sub-array with given sum

def subArraySum(arr, n, sum):
    # Pick a starting point
    for i in range(0, n):
        currentSum = arr[i]
        if (currentSum == sum):
            print("Sum found at indexes", i)
            return
        else:
            # Try all subarrays starting with 'i'
            for j in range(i + 1, n):
                currentSum += arr[j]
                if (currentSum == sum):
                    print("Sum found between indexes", i, "and", j)
                    return
    print("No Subarray Found")


# Driver Code
if __name__ == "__main__":
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    n = len(arr)
    sum = 23
    subArraySum(arr, n, sum)
