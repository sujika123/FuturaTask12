#K-th Largest Sum Contiguous Subarray

def kthLargestSum(arr, N, K):
    result = []
    #  Generate all subarrays
    for i in range(N):
        sum = 0
        for j in range(i, N):
            sum += arr[j]
            result.append(sum)

    # Sort in decreasing order
    result.sort(reverse=True)

    # return the Kth largest sum
    return result[K - 1]


# Driver's code
a = [20, -5, -1]
N = len(a)
K = 3

# Function call
print(kthLargestSum(a, N, K))