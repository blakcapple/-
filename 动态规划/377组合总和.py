# 给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。

# 题目数据保证答案符合 32 位整数范围。

from typing import List

# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         dp = [0] * (target + 1)
#         dp[0] = 1
#         # 对于不考虑元素顺序的组合问题，先遍历物品数量，再遍历容量大小；
#         # 对于考虑元素顺序的组合问题，则要反过来
#         # for v in nums:
#         #     for j in range(v, target+1):
#         #         dp[j] += dp[j-v]
#         for j in range(1, target+1):
#             for v in nums:
#                 if j < v:
#                     continue
#                 dp[j] += dp[j-v]
#         print(dp)
#         return dp[-1]
    
# s = Solution()
# nums = [1,2,3]
# target = 4
# print(s.combinationSum4(nums, target))


def combinationSum4( nums: List[int], target: int):
    dp = [0 for _ in range(target+1)]
    dp[0] = 1
    for size in range(1, target+1, 1):
        for item in nums:
            if item > size:
                continue
            dp[size] += dp[size-item] 
    print(dp)

nums = [1,2,3]
target = 4
combinationSum4(nums, target)