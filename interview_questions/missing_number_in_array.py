'''
https://practice.geeksforgeeks.org/problems/missing-number-in-array/0/?ref=self
Given an array of size n-1 and given that there are numbers from 1 to n with one missing, 
the missing number is to be found.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N.
The second line of each test case contains N-1 input C[i],numbers in array.
'''

def missingNumber(A):
    allNums = {i for i in range(1, len(A) + 2)}
    return (allNums - set(A)).pop()

if __name__ == '__main__':
    A = [1,2,3,5]
    print(missingNumber(A))
