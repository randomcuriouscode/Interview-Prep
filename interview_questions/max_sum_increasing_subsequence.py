'''https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence/0'''

def find_subsequences(A, start):
        # find all increasing subsequences in A starting from start
        all_subseq = []

        last_end_index = start + 1

        while last_end_index < len(A) - 1:
            subseq = [A[start]] #subseq starts at A[start]

            for i in range(last_end_index, len(A)):
                if  A[i] > subseq[-1]:
                    subseq.append(A[i])
                    last_end_index += 1
                elif i == len(A) - 1:
                    last_end_index += 1 # if end reached in this loop and no more consecutive
                    break # break and start next index over
                else:
                    last_end_index = i
                    break
            all_subseq.append(subseq)
        return all_subseq

def max_sum_subsequence(A):
    lstmap = {}

    for i, n in enumerate(A):
        subseq = find_subsequences(A, i)
        for l in subseq:
            lstmap[tuple(l)] = sum(l)
    return max(lstmap.items(), key=lambda k: k[1])


if __name__ == '__main__':
    A = [1,101,2,3,100,4,5]
    '''for a in (find_subsequences(A, i) for i, n in enumerate(A)):
        print(a)'''

    print(find_subsequences(A, 0))