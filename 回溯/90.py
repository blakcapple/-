# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        nums.sort()
        res.append([])
        def backtracking(start_idx, input, used):
            if start_idx >= len(input):
                return 
            for i in range(start_idx, len(input)):
                if i >= 1 and nums[i] == nums[i-1] and used[i-1] == False:
                    continue
                path.append(input[i])
                res.append(path[:])
                used[i] = True
                backtracking(i+1, input, used)
                used[i] = False
                path.pop()
                
        used = [False] * len(nums)
        backtracking(0, nums, used)
        return res

nums = [1,2,2]
s = Solution()
print(s.subsetsWithDup(nums))
    