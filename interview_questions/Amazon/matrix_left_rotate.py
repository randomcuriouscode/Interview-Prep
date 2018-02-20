import numpy as np
import sys

def left_rotate(A, M, N, K):
    A = A.reshape(M, N)

    for i, row in enumerate(A):
        A[i] = np.roll(row, -K)

    return A.reshape(M * N)

if __name__ == '__main__':
    A = np.array([1,2,3,4])
    s = left_rotate(A, 2, 2, 1)

    for i in s:
        sys.stdout.write('{} '.format(i))

    sys.stdout.write('\n')