'''https://practice.geeksforgeeks.org/problems/maximum-tip-calculator/0'''
import numpy as np

def max_tip(N, A, B, X, Y, n= 0):

    if n == len(A) or N == 0:
        return 0

    if X == 0 and Y > 0: # rahul cannot take more orders
        return max(B[n] + max_tip(N - 1, A, B, X, Y - 1, n + 1), # ankit takes the order
                    max_tip(N, A, B, X, Y, n + 1))  # ankit does not take order
    elif Y == 0 and X > 0: # ankit cannot take more orders
        return max(A[n] + max_tip(N - 1, A, B, X - 1, Y, n + 1), # rahul takes the order
                    max_tip(N, A, B, X, Y, n + 1)) # rahul does not take order
    elif Y == 0 and X == 0: # neither can take orders
        return 0
    else:
        return max(A[n] + max_tip(N - 1, A, B, X - 1, Y, n + 1), # rahul takes the order
                B[n] + max_tip(N - 1, A, B, X, Y - 1, n + 1), #ankit takes the order
                max_tip(N, A, B, X, Y, n + 1)) # nobody takes the order

def max_tip_efficient(N, A, B, X, Y, n = 0):
    '''
        incorrect, revisit if possible
    '''
    differences = [(A[i] - B[i], i) for (i, x) in enumerate(A)]

    # negative : ankit should take the order (Y - 1)
    # positive : rahul should take the order (X - 1)

    differences.sort(key=lambda x: x[0])
    indetDiff = []

    print(differences)

    x_iter, y_iter, i = 0, 0, 0
    max_tip = 0


    while x_iter < X and y_iter < Y and len(differences) > 1:
        rahul_takes = -differences[0][0] - differences[-1][0]
        if rahul_takes > 0: # rahul should take order if he can
            order = differences.pop(0)
            if x_iter < X:
                max_tip += A[order[1]]
                x_iter += 1
                i += 1
            else:
                indetDiff.append(order)
        elif rahul_takes < 0: # ankit should take order if he can
            order = differences.pop(-1)
            if y_iter < Y:
                max_tip += B[order[1]]
                y_iter += 1
                i += 1
            else:
                indetDiff.append(order)
        else:
            indetDiff.append(differences.pop(0))

    indetDiff.sort(key=lambda x: x[0])


    while x_iter < X and i < N:
        rahul_order = max(indetDiff)
        indetDiff.remove(rahul_order)
        max_tip += A[rahul_order[1]]
        x_iter += 1
        i += 1

    while y_iter < Y and i < N:
        ankit_order = min(indetDiff)
        indetDiff.remove(ankit_order)
        max_tip += B[ankit_order[1]]
        y_iter += 1
        i += 1
    print("x: {}, y: {}, max: {}".format(x_iter, y_iter, max_tip))

    return max_tip


if __name__ == '__main__':
    print(max_tip(5, [1,2,3,4,5], [5,4,3,2,1], 3, 3))
    print(max_tip(8, [1,4,3,2,7,5,9,6], [1,2,3,6,5,4,9,8], 4,4))
    print(max_tip(7, [8,7,15,19,16,16,18], [1,7,15,11,12,31,9], 3, 3))