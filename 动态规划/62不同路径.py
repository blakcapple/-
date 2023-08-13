
#一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

#机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

#问总共有多少条不同的路径？

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [[1 for _ in range(n)] for _ in range(m)]
#         dp[0][0] = 0
        
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
#         print(dp)
#         return dp[-1][-1]
    
# s = Solution()
# m = 3
# n = 2
# result = s.uniquePaths(m,n)
# print(result)

def fun(m, n):
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    if m == 1 or n == 1: 
        return  1
    for i in range(1,n+1):
        dp[1][i] = 1
    for j in range(1, m+1):
        dp[j][1] = 1
    for i in range(2, m+1):
        for j in range(2, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]
        
        
m = 3
n = 7
print(fun(m,n))