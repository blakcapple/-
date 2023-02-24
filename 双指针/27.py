#给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并原地修改输入数组。

# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

# 示例 1: 给定 nums = [3,2,2,3], val = 3, 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。 你不需要考虑数组中超出新长度后面的元素。

# 示例 2: 给定 nums = [0,1,2,2,3,0,4,2], val = 2, 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

# 你不需要考虑数组中超出新长度后面的元素。

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        left_idx = 0 
        right_idx = 0 
        while right_idx <= (len(nums)-1) and left_idx <= right_idx:
            if nums[right_idx] == val:
                right_idx += 1
            else:
                nums[left_idx] = nums[right_idx]
                right_idx += 1
                left_idx += 1
        return (left_idx)
# 一种更简洁的写法
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         fast_index = 0
#         slow_index = 0 
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[slow_index] = nums[i]
#                 slow_index += 1

#         return slow_index
nums = [3,2,2,3]
val = 3
s = Solution()
print(s.removeElement(nums, val))
print(nums)