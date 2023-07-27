#Merge Sort Tree for Range Order Statistics

import math

# maximum size of the array
MAX = 100

def buildTree(treeIndex, left, right, a, tree):
	# base case
	if left == right:
		tree[treeIndex] = a[left][1]
		return

	# recursive case
	mid = (left + right) // 2
	buildTree(2 * treeIndex, left, mid, a, tree)
	buildTree(2 * treeIndex + 1, mid + 1, right, a, tree)

	tree[treeIndex] = min(tree[2 * treeIndex], tree[2 * treeIndex + 1])

def query(treeIndex, left, right, l, r, a, tree):
	# base case
	if l <= left and r >= right:
		return tree[treeIndex]

	# recursive case
	mid = (left + right) // 2
	if r <= mid:
		return query(2 * treeIndex, left, mid, l, r, a, tree)
	elif l > mid:
		return query(2 * treeIndex + 1, mid + 1, right, l, r, a, tree)
	else:
		leftResult = query(2 * treeIndex, left, mid, l, r, a, tree)
		rightResult = query(2 * treeIndex + 1, mid + 1, right, l, r, a, tree)
		return min(leftResult, rightResult)

if __name__ == '__main__':
	arr = [3, 2, 5, 1, 8, 9]
	n = len(arr)

	# vector of pairs of form {element, index}
	v = []
	for i in range(n):
		v.append((arr[i], i))

	# sort the vector
	v.sort()

	# Construct segment tree
	tree = [0] * (4 * n)
	buildTree(1, 0, n - 1, v, tree)

	# Answer queries
	# kSmallestIndex hold the index of the kth smallest number
	kSmallestIndex = query(1, 0, n - 1, 2, 5, v, tree)
	print(arr[kSmallestIndex])

	kSmallestIndex = query(1, 0, n - 1, 1, 6, v, tree)
	print(arr[kSmallestIndex])
