'''https://practice.geeksforgeeks.org/problems/equilibrium-point/0'''
def find_equilibrium(A):
    if len(A) < 3:
        return -1

    sum_before = A[0]
    sum_after = sum(A) - A[1] - A[0]

    idx = 1 # the equilibrium point

    if sum_before == sum_after:
        return idx


    while idx < len(A) - 1:
        idx += 1
        sum_before += A[idx - 1]
        sum_after -= A[idx]

        if sum_before == sum_after:
            return idx # 0 based

        
    return -1

if __name__ == '__main__':
    A = [1,3,5,2,2]
    print(find_equilibrium(A))