# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        nums.sort()
        def backtracking(used): 
            if len(path) == len(nums):
                res.append(path[:])
                return 
            used_set = set() # 用于同一个树层的去重
            for i in range(0, len(nums)):
                if used[i] or (nums[i] in used_set):
                    continue
                path.append(nums[i])
                used_set.add(nums[i])
                used[i] = True
                backtracking(used)
                path.pop()
                used[i] = False
        used = [False] * len(nums)
        backtracking(used)
        return res
    
s = Solution()
nums = [1, 1]
print(s.permuteUnique(nums))