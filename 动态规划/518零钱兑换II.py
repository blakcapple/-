"""给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
"""
from typing import List
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         n = len(coins)
#         dp = [0] * (amount + 1)
#         dp[0] = 1
#         for v in coins:
#             for j in range(v, amount+1): # 正序遍历
#                 dp[j] += dp[j-v]
#         print(dp)
#         return dp[-1]
    
# s = Solution()
# amount = 5
# coins = [1, 2, 5]
# print(s.change(amount, coins))

def fun(amount: int, coins: List[int]):
    n = len(coins)
    dp = [0 for _ in range(amount+1)] 
    dp[0] = 1
    for i in range(n):
        for j in range(amount+1):
            if coins[i] > j:
                continue
            dp[j] += dp[j-coins[i]]
    print(dp)
    return dp[-1]

amount = 5
coins = [1, 2, 5]
fun(amount, coins)