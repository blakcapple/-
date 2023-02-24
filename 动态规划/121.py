# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 二维dp,第一个维度表示天数，第二个维度表示是否持有股票 0 表示持有 1表示不持有
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0] = -prices[0] # 第一天持有即买入股票
        dp[0][1] = 0 
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i]+dp[i-1][0])
        print(dp)
        return max(dp[-1][0], dp[-1][1])
    
s = Solution()
prices = [7,6,4,3,1]
print(s.maxProfit(prices))