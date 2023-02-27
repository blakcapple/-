# 给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。

# 数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。
from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        def backtracking(start_idx, input, used):
            if start_idx >= len(input):
                return 
            used_list = set()
            for i in range(start_idx, len(input)):
                if path and input[i] < path[-1] or input[i] in used_list:
                    continue
                path.append(input[i])
                if len(path) >= 2:
                    res.append(path[:])
                used_list.add(input[i])
                backtracking(i+1, input, used)
                path.pop()
        used = [False] * len(nums)
        backtracking(0, nums, used)
        
        return res
    
s = Solution()
nums = [4,4,1,1,1,1]
print(s.findSubsequences(nums))
        
                
        