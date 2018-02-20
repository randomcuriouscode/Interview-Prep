'''https://practice.geeksforgeeks.org/problems/start-elements/0'''

def find_star_super(A, N):
    star_elements = []
    super_star_elements = []

    if len(A) == 0:
        star_elements.append(-1)
        super_star_elements.append(-1)
        return (star_elements, super_star_elements)

    elif len(A) == 1:
        star_elements.append(A[0])
        super_star_elements.append(A[0])
        return (star_elements, super_star_elements)

    max_to_i = A[-1]
    star_elements.append(A[-1])

    for i in range(N - 2, -1, -1):
        if max_to_i < A[i]:
            max_to_i = A[i]
            star_elements.append(A[i])

    if A.count(max_to_i) == 1:
        super_star_elements.append(max_to_i)

    if len(super_star_elements) == 0:
        super_star_elements.append(-1)

    return (sorted(star_elements), super_star_elements)

if __name__ == '__main__':
    print(find_star_super([8,6,5], 3))