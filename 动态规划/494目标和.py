##给你一个整数数组 nums 和一个整数 target 。

#向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

#例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
#返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if abs(target) > total_sum:
            return 0 
        if (target + total_sum) % 2 != 0:
            return 0 
        left = (target + total_sum)//2
        dp = [0] * (left+1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(left, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        print(dp)
        return dp[-1]
    
s = Solution()
nums = [1,1,1,1,1]
target = 3
print(s.findTargetSumWays(nums, target))