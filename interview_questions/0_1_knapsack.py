import numpy as np
called = 0

def z_o_knapsack(W, wt, val, n):
    global called
    called += 1

    if n == -1 or W == 0: # base case, 0 items or 0 weight left in knapsack
        return 0

    if W < wt[n]:
        return z_o_knapsack(W, wt, val, n - 1) # if nth item too heavy, cannot be included

    else:
        return max(z_o_knapsack(W, wt, val, n - 1), # value with nth item excluded
                    val[n] + z_o_knapsack(W - wt[n], wt, val, n - 1) # value with nth item included
                )

def z_o_knapsack_memoized(W, wt, val, n, memo=None):
    global called
    called += 1

    if memo == None:
        memo = np.zeros((n+1, W+1))

    if n == -1 or W == 0: # base case, 0 items or 0 weight left in knapsack
        return 0

    if memo[n, W] != 0:
        return memo[n, W]

    elif W < wt[n]:
        mem_val = z_o_knapsack(W, wt, val, n - 1) if memo[n-1, W] == 0 else memo[n-1, W] # if nth item too heavy, cannot be included
        memo[n,W] = mem_val
        return mem_val

    else:
        mem_val = max(z_o_knapsack(W, wt, val, n - 1) if memo[n-1, W] == 0 else memo[n-1, W] == 0, # value with nth item excluded
                    val[n] + z_o_knapsack(W - wt[n], wt, val, n - 1) 
                        if memo[n-1, W - wt[n]] == 0 else memo[n-1, W - wt[n]] # value with nth item included
                )
        memo[n, W] = mem_val
        return mem_val

def z_o_knapsack_btm_up(W, wt, val, n):
    global called
    memo = np.zeros((n + 1, W + 1))

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            called += 1
            if i == 0 or w == 0:
                memo[i, w] = 0

            elif wt[i - 1] > w:
                memo[i, w] = memo[i - 1, w]
            else:
                memo[i, w] = max(memo[i - 1, w],
                    val[i - 1] + memo[i - 1, w - wt[i - 1]]
                    )

    print(memo)
    return memo[n, W]


if __name__ == '__main__':
    val = [1,4,5,7]
    wt = [1,3,4,5]
    W = 7

    #print(z_o_knapsack_memoized(W, wt, val, len(val) - 1))
    #print(z_o_knapsack(W, wt, val, len(val) - 1))
    print(z_o_knapsack_btm_up(W, wt, val, len(val)))
    print(called)