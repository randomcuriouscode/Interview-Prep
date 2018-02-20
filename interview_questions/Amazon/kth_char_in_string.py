'''https://practice.geeksforgeeks.org/problems/find-k-th-character-in-string/0'''

def find_kth(m, k, n):
    # apply n iterations to m where 0 -> 01 and 1 -> 10
    mbin = bin(m)[2:]

    for i in range(n):
        mbin = ''.join(list(map(lambda x: '01' if x == '0' else '10' if x == '1' else None, mbin)))

    print(mbin)
    return mbin[k]

if __name__ == '__main__':
    print(find_kth(5,5,3))
    print(find_kth(11,6,4))