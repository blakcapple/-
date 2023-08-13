# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

# from typing import List
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total_sum = sum(nums)
#         dp = [0] * 20001
#         dp[0] = 0
#         if total_sum % 2 !=0:
#             return False
#         else:
#             target = total_sum // 2
#             for i in range(len(nums)):
#                 for j in range(target, nums[i]-1,-1):
#                     dp[j] = max(dp[j], dp[j-nums[i]]+nums[i])
#             return target == dp[target]
# s = Solution()
# nums = [1,5,11,5]
# print(s.canPartition(nums))                    


def fun(nums):
    sum_of_nums = sum(nums)
    if sum_of_nums % 2 == 1:
        return False
    else:
        n = sum_of_nums // 2 
        dp = [0 for i in range(n+1)]
        sort_nums = sorted(nums, reverse=True)
        for item in nums:
            for i in range(n, 0, -1):
            # for i in range(1, n+1):
                if item > i:
                    continue
                dp[i] = max(dp[i], dp[i-item]+ item)
        print(dp)
        return n == dp[-1]
    
print(fun([1,3,4,4]))

