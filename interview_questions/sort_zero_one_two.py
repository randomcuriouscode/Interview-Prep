'''
https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0
'''

def sort_z_o_t(A):
    count = [0 for i in range(3)]

    for i in A:
        count[i] += 1
    aIdx = 0
    for i, n in enumerate(count):
        while n > 0:
            A[aIdx] = i
            n -= 1
            aIdx += 1

if __name__ == '__main__':
    A = [0, 2, 1, 2, 0]
    sort_z_o_t(A)
    print(A)