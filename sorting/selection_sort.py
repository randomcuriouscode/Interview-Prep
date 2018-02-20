def select(A, start):
    minimum = A[start]
    min_idx = start

    for i in range(start + 1, len(A)):
        if minimum > A[i]: 
            minimum = A[i]
            min_idx = i

    return (minimum, min_idx)
def selection_sort(A):
    for i in range(len(A)):
        minimum = select(A, i)

        temp = A[i]
        A[i] = minimum[0]
        A[minimum[1]] = temp

if __name__ == "__main__":
    A = [4,1,3,9,7]
    selection_sort(A)
    print(A)
