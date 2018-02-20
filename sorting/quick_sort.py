import random

def partition(arr, low, high):
    # select pivot

    origPI = random.randint(low,high)
    pivot, arr[low], arr[origPI] = arr[origPI], arr[origPI], arr[low]

    leftI, rightI = low - 1, high + 1

    while True:
        # keeps swapping pivot with first item less than, then greater than, then less than
        condition = True 

        while condition:
            leftI += 1

            condition = arr[leftI] < pivot # find index of first element in left >= pivot

        condition = True

        while condition:
            rightI -= 1

            condition = arr[rightI] > pivot # find index of first element in right <= pivot

        if leftI >= rightI: #if indices have converged
            return rightI

        arr[leftI], arr[rightI] = arr[rightI], arr[leftI] # swap out of place elements to correct location

''' 
i1: 
leftI = 0
rightI = 7
90, 83, 84, 85, 86, 87, 88, 89 
swap
89, 83, 84, 85, 86, 87, 88, 90

i2:
leftI = 7
rightI = 6

'''

def quick_sort(arr, low, high):
    '''
    arr: array to operate on
    low: start index in arr for quicksort
    high: end index in arr for quicksort
    '''
    if len(arr) <= 1: 
        return 

    if low < high:
        pivotIndex = partition(arr,low,high)

        quick_sort(arr, low, pivotIndex) # sort to left of pivot
        quick_sort(arr, pivotIndex + 1, high) # sort to right of pivot

if __name__ == '__main__':
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    quick_sort(A, 0, len(A) - 1)
    print(A)