'''
https://practice.geeksforgeeks.org/problems/common-subsequence/0
Given two strings a and b print whether they contain any common subsequence (non empty) 
or not.

'''

def find_common(A, B):
    sA = set(A)
    sB = set(B)

    return sA.intersection(sB) != set()
