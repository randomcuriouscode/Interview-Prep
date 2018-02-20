import math

def is_prime(n):
    if n == 1:
        return False
    return all(n % i for i in range(2, math.floor(n ** .5)))

def prime_set_bits_in_range(R, L):
    count_prime = 0
    for n in range(R, L + 1):
        set_bits = str(bin(n)).count('1')
        if is_prime(set_bits):
            count_prime += 1

    return count_prime

if __name__ == '__main__':
    print(prime_set_bits_in_range(6,10))