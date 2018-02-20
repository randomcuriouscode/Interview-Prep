
'''{{60, 10}, {100, 20}, {120, 30}} (value, weight)'''

def fractional_knapsack(arr, capacity):
    '''
        arr : the items
    '''
    weighted_arr = []
    knapsack = []
    weight = 0
    value = 0

    for item in arr:
        weighted_arr.append((item[0] / item[1], item[0], item[1]))
    
    weighted_arr.sort(key=lambda x:x[0])

    while weight < capacity and len(weighted_arr) > 0:
        item = weighted_arr.pop()
        item_multiplier = (capacity - weight) / item[2]
        if item_multiplier >= 1:
            knapsack.append((1, item[1], item[2]))
            value += item[1]
            weight += item[2]
        else:
            knapsack.append((item_multiplier, item[1], item[2]))
            value += item_multiplier * item[1]
            weight += item_multiplier * item[2]

    return knapsack, weight, value

if __name__ == '__main__':
    A = [(60,10), (100,20), (120,30)]
    a, b, c = fractional_knapsack(A, 50)
    print((a,b,c))