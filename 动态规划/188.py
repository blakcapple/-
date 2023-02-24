# 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:return 0
        state_num = 1+2*k
        dp = [[0 for _ in range(state_num)] for _ in range(len(prices))]
        for idx in range(1, state_num):
            if idx % 2 == 1:
                dp[0][idx] = -prices[0]
        for i in range(1, len(prices)):
            for j in range(1, state_num):
                if j % 2 == 1:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]-prices[i])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+prices[i])
        print(dp)
        return dp[-1][-1]

s = Solution()
k = 2
prices = [3,2,6,5,0,3]
print(s.maxProfit(k, prices))