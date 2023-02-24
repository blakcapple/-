# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        dp = [0] * 20001
        dp[0] = 0
        if total_sum % 2 !=0:
            return False
        else:
            target = total_sum // 2
            for i in range(len(nums)):
                for j in range(target, nums[i]-1,-1):
                    dp[j] = max(dp[j], dp[j-nums[i]]+nums[i])
            return target == dp[target]
s = Solution()
nums = [1,5,11,5]
print(s.canPartition(nums))                    
