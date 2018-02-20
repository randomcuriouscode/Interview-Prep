'''
    https://practice.geeksforgeeks.org/problems/positive-and-negative-elements/0
'''
def pos_neg_pairs(A):
    pos = []
    neg = []

    for i in A:
        if i >= 0:
            pos.append(i)
        else:
            neg.append(i)

    return [ele for tup in zip(pos,neg) for ele in tup]

