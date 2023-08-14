# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。
# 这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
# 同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
from typing import List
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         def rob_fun(nums: List[int]) -> int:
#             n = len(nums)
#             dp = [0] * (n)
#             dp[0] = nums[0]
#             if n == 1:
#                 return nums[0]
#             dp[1] = max(nums[0], nums[1])
#             for i in range(2, n):
#                 dp[i] = max(dp[i-1], dp[i-2]+nums[i])
#             print(dp)
#             return dp[-1]
#         # 去掉尾元素
#         nums1 = nums[:-1]
#         # 去掉头元素
#         nums2 = nums[1:]
#         result1 = rob_fun(nums1)
#         result2 = rob_fun(nums2)
#         return max(result1, result2)
# s = Solution()
# nums = [2,3,2]
# print(s.rob(nums))
        
def rob(nums: List[int]):
    if len(nums) == 1:
        return nums[0]
    nums1 = nums[:-1]
    nums2 = nums[1:]
    def _fun(nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]
    
    return(max(_fun(nums1), _fun(nums2)))

nums = [1,2,3,1]
print(rob(nums))
        