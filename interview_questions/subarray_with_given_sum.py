'''
    https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0/?ref=self
    Given an unsorted array of non-negative integers, find a 
    continuous sub-array which adds to a given number.

    Input:

    The first line of input contains an integer T denoting the number of test cases. 
    Then T test cases follow. Each test case consists of two lines. 
    The first line of each test case is N and S, where N is the size of array and S is the sum. 
    The second line of each test case contains N space separated integers denoting the array 
    elements
'''

def find_contiguous_adds_to(A, s):
    if len(A) == 0:
        return -1
    elif len(A) == 1:
        return (0,0) if A[0] == s else -1

    curSum = A[0]
    start = 0
    end = 1

    while start <= end and curSum <= s and end < len(A):
        if curSum + A[end] < s:
            curSum += A[end]
            end += 1
        elif curSum + A[end] == s:
            curSum += A[end]
            return start + 1, end + 1
        else:
            curSum -= A[start]
            start += 1

    return -1

def find_contiguous_posneg_adds_to(A, s):
    if len(A) == 0:
        return -1
    elif len(A) == 1:
        return (0,0) if A[0] == s else -1

    sumMap = dict()
    curSum = 0

    for i, num in enumerate(A):
        curSum += num

        if curSum == s:
            return (0, i)

        elif sumMap.get(curSum - s, None) is not None:
            return sumMap.get(curSum - s) + 1, i 
            #if value of difference between current sum and s is in map, exclude that value (subtract it)
            #and return index of solution as 1+ index of subarray from 0..A[sumMap[curSum - s]]

        sumMap[curSum] = i


if __name__ == '__main__':
    A = [1,2,-3, 3, 3, 7,5]
    s = 12

    #print(find_contiguous_adds_to(A,s))
    print(find_contiguous_posneg_adds_to(A,s))
