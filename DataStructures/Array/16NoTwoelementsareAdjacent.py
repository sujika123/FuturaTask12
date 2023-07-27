#Maximum sum such that no two elements are adjacent

def rec(nums, idx):
    if idx >= len(nums):
        return 0
    return max(nums[idx] + rec(nums, idx + 2), rec(nums, idx + 1))


def findMaxSum(arr, N):
    return rec(arr, 0)


# Driver Code
if __name__ == "__main__":
    # Creating the array
    arr = [5, 5, 10, 100, 10, 5]
    N = len(arr)

    # Function call
    print(findMaxSum(arr, N))