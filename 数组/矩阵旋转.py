def rotate(matrix):
    n = len(matrix)
    matrix_new = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(j):
            matrix_new[j][n-i-1] = matrix[i][j]
    return matrix_new

# 原地旋转
# 四个构成一个循环
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]