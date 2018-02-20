def find_subarray(A, i):
    k = A[i]
    solutions = [A.pop(i)]
    for n in range(i - 1, -1, -1): # search left
        if k >= A[n]:
            solutions.insert(0, A.pop(n))
        else:
            break

    for n in range(-(len(A) - i - 1), 0): # search right
        if k >= A[n]:
            solutions.append(A.pop(n))
        else:
            break

    return solutions

def sum_len_no_subarray(A, k):
    sum_len = 0
    for i, n in enumerate(A):
        if n == k:
            subarr = find_subarray(A, i)
            sum_len += len(subarr)

    return sum_len

if __name__ == '__main__':
    A = [2,1,4,9,2,3,8,3,4]
    K = 4

    print(sum_len_no_subarray(A, K))