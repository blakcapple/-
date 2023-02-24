# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:return 1
        # dp数组含义为以nums[i]为结尾的子序列的最大长度，这样子才能做序列比较
        dp = [1] * n
        # dp[0] = 1
        result = 0
        for i in range(1,n):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            result = max(result, dp[i])
        print(dp)
        return result
    
s =  Solution()
nums = [10,9,2,5,3,7,101,18]
print(s.lengthOfLIS(nums))