'''https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0
Given an array containing both negative and positive integers. 
Find the contiguous sub-array with maximum sum.
 
Input:
The first line of input contains an integer T denoting the number of test cases. 
The description of T test cases follows. The first line of each test case contains 
a single integer N denoting the size of array. The second line contains N space-separated 
integers A1, A2, ..., AN denoting the elements of the array.
 
Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.
 
Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 1000
-100 ≤ A[i] <= 100
'''

def find_max_naive(A):
    def find_contiguous_subarray(A, n):
        # find the maximum contiguous subarray starting from n onwards by checking
        # all possible subarrays including n onwards
        if n == len(A) - 1:
            return A[n], n, n
        else:
            curSum = A[n]

            sums = []
            sums.append((A[n], n, n))

            for i in range(n + 1, len(A)):
                curSum += A[i]
                sums.append((curSum, n, i))

            return max(sums, key=lambda k: k[0])
        
    sums = []
    for i in range(len(A)):

        sums.append(find_contiguous_subarray(A,i))

    return max(sums, key=lambda k: k[0])

def find_max(A):
    currentMax = float("-inf"), -1, -1

    maxAtIndex = 0
    indexStart = 0

    for i in range(0, len(A)):
        maxAtIndex = maxAtIndex + A[i]

        if currentMax[0] < maxAtIndex:
            currentMax = maxAtIndex, indexStart, i

        if maxAtIndex < 0:
            maxAtIndex = 0
            indexStart = i + 1

    return currentMax

if __name__ == '__main__':
    A = [-1,2,3, -1, 6]
    print(find_max_naive(A))
    print(find_max(A))