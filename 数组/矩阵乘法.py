def matrix_multiplication(A, B):
    result = []
    for i in range(len(A)):
        result.append([0] * [len(B[0])])
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]