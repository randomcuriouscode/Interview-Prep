import numpy as np
import heapq

'''https://www.youtube.com/watch?v=eaYX0Ee0Kcg'''

def find_k_closest(L, k):
    q = []

    for a in L:
        heapq.heappush(q, (a[0] ** 2 + a[1] ** 2, a))

    return [k[1] for k in heapq.nsmallest(k, q, lambda v: v[0])]

if __name__ == "__main__":
    points = [(-2,4), (0,-2), (-1,0), (3,5), (-2,-3), (3,2)]
    print(find_k_closest(points, 2))