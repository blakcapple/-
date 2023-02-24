# 给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

# 在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

# 返回 你能获得的 最大 利润 。
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 二维dp,第一个维度表示天数，第二个维度表示是否持有股票 0 表示持有 1表示不持有
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0] = -prices[0] # 第一天持有即买入股票
        dp[0][1] = 0 
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i]+dp[i-1][0])
        print(dp)
        return max(dp[-1][0], dp[-1][1])
    
s = Solution()
prices = [7,1,5,3,6,4]
x = s.maxProfit(prices=prices)
print(x)