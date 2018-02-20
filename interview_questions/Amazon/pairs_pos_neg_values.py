'''https://practice.geeksforgeeks.org/problems/pairs-with-positive-negative-values/0'''

from collections import defaultdict
import heapq
import re

def pos_neg_pairs(A):
    count = defaultdict(lambda: [0,0])

    for i, n in enumerate(A):
        if n < 0:
            count[abs(n)][0] += 1
        else:
            count[n][1] += 1

    pairs = []

    for k,v in count.items():
        if v[0] == v[1]:
            for i in range(v[0]):
                pairs.append((-k, k))

    heapq.heapify(pairs)

    return [heapq.heappop(pairs) for i in range(len(pairs))]

if __name__ == '__main__':
    A = [1,-3,2,3,6,-1]
    print(''.join(pos_neg_pairs(A)))
    print(re.sub(r'[\[\(-,\)\]]','',''.join(pos_neg_pairs(A))))