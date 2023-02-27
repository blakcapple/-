# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        res.append([])
        def backtracking(start_idx, input):
            if start_idx >= len(input):
                return 
            for i in range(start_idx, len(input)):
                path.append(input[i])
                res.append(path[:])
                backtracking(i+1, input)
                path.pop()
                
        backtracking(0, nums)
        return res
    
s = Solution()
nums = [1,2,3]
print(s.subsets(nums))