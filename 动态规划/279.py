#给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

#完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

class Solution:
    def numSquares(self, n: int) -> int:
        num = [x**2 for x in range(1, 101)]
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in num:
            for j in range(i, n+1):
                dp[j] = min(dp[j], dp[j-i]+1)
        print(dp)
        return dp[-1]
    
s = Solution()
n = 13
print(s.numSquares(n))