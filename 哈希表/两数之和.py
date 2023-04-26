# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

# 你可以按任意顺序返回答案。
from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record_map = dict()
        for idx, item in enumerate(nums):
            expect = target - item
            if expect not in record_map.keys():
                record_map[item] = idx
            else:
                expect_idx = record_map[expect]
                return [idx, expect_idx]


nums = [2,7,11,15]  
target = 9          
s = Solution()
print(s.twoSum(nums, target))