def matrix_multiply(A, B):
    # Multiply two matrices A and B
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += (A[i][k] * B[k][j]) % 2147483647
                result[i][j] %= 2147483647
    return result

def matrix_power(M, n):

    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, M)
        M = matrix_multiply(M, M)
        n //= 2
    return result

def fibonacci_modulo(n):

    if n <= 1:
        return n
    
    base_matrix = [[1, 1], [1, 0]]


    result_matrix = matrix_power(base_matrix, n)
    return result_matrix[0][0] % 2147483647


n = int(input())


result = fibonacci_modulo(n)

print(result)