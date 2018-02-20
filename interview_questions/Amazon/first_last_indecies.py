def find_first_last(A, x):
    iFirst, iLast = -1,-1
    for i, n in enumerate(A):
        last = A[-i - 1]
        if iLast == -1 and last == x:
            iLast = -i - 1 + len(A) if i != 0 else 0
        if iFirst == -1 and n == x:
            iFirst = i
    return iFirst, iLast


if __name__ == '__main__':
    A = [1,3,5,5,5,5,7,123,125]
    x = 7

    print(find_first_last(A, x))