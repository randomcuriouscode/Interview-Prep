import numpy as np
import sys

'''
Google internship question 2.
Given a matrix with only 0s and 1s, where 0 represents a wall and 1 represents a path, return if there is a path from first to last row.
'''

def path_exists(A, visited, m=0, n=0):
    if m == A.shape[0] - 1:
        return A[m,n] == 1
    else:
        visited[m,n] = 1
        return A[m,n] == 1 and (path_exists(A, visited, m+1, n) or path_exists(A, visited, m, n+1) if n + 1 >= 0 and n + 1 < A.shape[1] and not visited[m, n+1]
             else False or path_exists(A, visited, m, n - 1) if n - 1 >= 0 and n - 1 < A.shape[1] and not visited[m, n - 1] else False) 

def path_find(A):
    for i in range(A.shape[1]):
        visited = np.zeros(A.shape)
        pe = path_exists(A, visited, 0, i)
        print("{},{} : {}".format(0, i, pe))

if __name__ == "__main__":
    A = np.array([[0,1,1,1,1],[0,1,0,0,0],[0,1,1,0,0], [1,0,1,0,0], [1,1,1,0,0]])
    path_find(A)

