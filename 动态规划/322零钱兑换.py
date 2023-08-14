#给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

#计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

#你可以认为每种硬币的数量是无限的。
from typing import List
# import numpy as np
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [float('inf')] * (amount+1)
#         dp[0] = 0
#         for coin in coins:
#             for i in range(coin, amount+1):
#                 dp[i] = min(dp[i], dp[i-coin]+1)
#         for idx, value in enumerate(dp):
#             if value == 13:
#                 dp[idx] = -1
#         print(dp)
#         return dp[-1]
    
# s = Solution()
# coins = [1,2,5]
# amount = 100
# print(s.coinChange(coins, amount))

def coinChange(coins: List[int], amount: int):
    dp = [float('inf') for _ in range(amount+1)]
    dp[0] = 0
    for item in coins:
        for size in range(item, amount+1):
            dp[size] = min(dp[size-item] + 1, dp[size])
    if dp[-1] == float('inf'):
        return -1
    else:
        return dp[-1]
coins = [1, 2, 5]
amount = 11
coinChange(coins, amount)