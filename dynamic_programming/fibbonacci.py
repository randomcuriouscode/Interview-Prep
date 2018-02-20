def fib(n):
    if n <= 1: 
        return n
    tab = [i for i in range(n+1)]
    tab[0] = 0
    tab[1] = 1

    for i in range(2, n + 1):
        tab[i] = tab[i-1] + tab[i-2]

    return tab[n]

if __name__ == '__main__':
    print(fib(4))