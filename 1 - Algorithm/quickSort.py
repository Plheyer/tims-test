def quickSort(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    L.pop(0)
    L1 = quickSort([i for i in L if i <= pivot])
    L2 = quickSort([i for i in L if i > pivot])
    return L1 + [pivot] + L2

print(quickSort([4, 2, 9, 1, 3, 7, 1, 6, 4, 12, 65, 4, 1, 56, 4, 1, 3, 4, 1, 8, 7, 9, 2, 1, 65, 4, 1]))

# This algorithm is very easy to implement. However, it's not the most efficient. We should not use it every time.
# We should use it only when we need something easy to implement with no efficicency requirements
# Additionally, it also very depend on the chosen 'pivot'