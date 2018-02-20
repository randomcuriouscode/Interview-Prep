'''https://practice.geeksforgeeks.org/problems/check-if-array-contains-contiguous-integers-with-duplicates-allowed/0'''

import heapq

def is_contiguous(A):
    if len(A) <= 1:
        return True
    T = list(A)

    heapq.heapify(T)

    prev_item = heapq.heappop(T)

    for i in range(1, len(A)):
        cur_item = heapq.heappop(T)

        if cur_item - prev_item > 1:
            return False

        prev_item = cur_item

    return True

if __name__ == '__main__':
    A = [4, 2, 6, 3, 3, 3, 5]
    print(is_contiguous(A))