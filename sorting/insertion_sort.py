def insertion_sort(A):
    if len(A) <= 1:
        return
    sortedIdx = 0
    for i in range(sortedIdx + 1, len(A)):
        toSort = A[i]
        for j in range(sortedIdx, -1, -1):
            if toSort < A[j]:
                A[j], A[j + 1] = A[j + 1], A[j]
            elif toSort > A[j]:
                break

        sortedIdx += 1

if __name__ == '__main__':
    A = [11, 12, 13, 5, 6]
    insertion_sort(A)
    print(A)