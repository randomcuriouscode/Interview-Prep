def bubble_sort(A, compare_func):
    if len(A) <= 1:
        return
    swapoccurred = True
    while swapoccurred:
        swapoccurred = False
        for i in range(len(A) - 1):
            if compare_func(A[i], A[i+1]):
                A[i], A[i+1] = A[i+1], A[i]
                swapoccurred = True

if __name__ == '__main__':
    A = [5,1,4,2,8]
    bubble_sort(A, lambda a,b: a < b)
    print(A)