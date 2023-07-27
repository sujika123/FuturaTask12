#Search an element in a sorted and pivoted array

def search_rotated_array(arr, key):
    n = len(arr)
    for i in range(n):
        if arr[i] == key:
            return i
    return -1


arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 3
index = search_rotated_array(arr, key)
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")

