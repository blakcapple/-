# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        def backtracking(used):# used 数组表示在纵向递归的时候是否用到了该数字
            if len(path) == len(nums):
                res.append(path[:])
                return 
            for i in range(0, len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtracking(used)
                path.pop()
                used[i] = False
        used = [False] * len(nums)
        backtracking(used)
        return res
         
s = Solution()
nums = [1,2,3]
print(s.permute(nums))