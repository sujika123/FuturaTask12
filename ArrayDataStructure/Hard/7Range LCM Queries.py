#Range LCM Queries

# LCM of given range queries using Segment Tree
MAX = 1000

# allocate space for tree
tree = [0] * (4 * MAX)

# declaring the array globally
arr = [0] * MAX


# Function to return gcd of a and b


def gcd(a: int, b: int):
    if a == 0:
        return b
    return gcd(b % a, a)


# utility function to find lcm


def lcm(a: int, b: int):
    return (a * b) // gcd(a, b)


# Function to build the segment tree
# Node starts beginning index of current subtree.
# start and end are indexes in arr[] which is global


def build(node: int, start: int, end: int):
    # If there is only one element
    # in current subarray
    if start == end:
        tree[node] = arr[start]
        return

    mid = (start + end) // 2

    # build left and right segments
    build(2 * node, start, mid)
    build(2 * node + 1, mid + 1, end)

    # build the parent
    left_lcm = tree[2 * node]
    right_lcm = tree[2 * node + 1]

    tree[node] = lcm(left_lcm, right_lcm)


# Function to make queries for array range )l, r).
# Node is index of root of current segment in segment
# tree (Note that indexes in segment tree begin with 1
# for simplicity).
# start and end are indexes of subarray covered by root
# of current segment.


def query(node: int, start: int,
          end: int, l: int, r: int):
    # Completely outside the segment,
    # returning 1 will not affect the lcm;
    if end < l or start > r:
        return 1

    # completely inside the segment
    if l <= start and r >= end:
        return tree[node]

    # partially inside
    mid = (start + end) // 2
    left_lcm = query(2 * node, start, mid, l, r)
    right_lcm = query(2 * node + 1,
                      mid + 1, end, l, r)
    return lcm(left_lcm, right_lcm)


# Driver Code
if __name__ == "__main__":
    # initialize the array
    arr[0] = 5
    arr[1] = 7
    arr[2] = 5
    arr[3] = 2
    arr[4] = 10
    arr[5] = 12
    arr[6] = 11
    arr[7] = 17
    arr[8] = 14
    arr[9] = 1
    arr[10] = 44

    # build the segment tree
    build(1, 0, 10)

    # Now we can answer each query efficiently

    # Print LCM of (2, 5)
    print(query(1, 0, 10, 2, 5))

    # Print LCM of (5, 10)
    print(query(1, 0, 10, 5, 10))

    # Print LCM of (0, 10)
    print(query(1, 0, 10, 0, 10))