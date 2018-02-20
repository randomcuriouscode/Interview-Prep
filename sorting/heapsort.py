import heapq

def heapsort(A):
    heapq.heapify(A)
    l = []
    while len(A) > 0:
        l.append(heapq.heappop(A))
    return l

if __name__ == '__main__':
    A = [i for i in range(10,-1,-1)]
    print(heapsort(A))