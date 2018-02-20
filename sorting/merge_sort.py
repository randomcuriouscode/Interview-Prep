import sys
sys.setrecursionlimit(20)
def merge(left, right):
    merged = []

    leftIndex, rightIndex = 0, 0

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]:
            merged.append(left[leftIndex])
            leftIndex += 1
        else:
            merged.append(right[rightIndex])
            rightIndex += 1

    while leftIndex < len(left):
        merged.append(left[leftIndex])
        leftIndex += 1
    while rightIndex < len(right):
        merged.append(right[rightIndex])
        rightIndex += 1

    return merged

def mergeSort(A):
    if len(A) <= 1:
        return A

    mid = len(A) // 2

    left = A[0 : mid]
    right = A[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left,right)



if __name__ == '__main__':
    A = [38, 27, 43, 3, 9, 82, 10]
    print(mergeSort(A))