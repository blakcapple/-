##给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
# 请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

#0 <= a, b, c, d < n
#a、b、c 和 d 互不相同
#nums[a] + nums[b] + nums[c] + nums[d] == target
#你可以按 任意顺序 返回答案 。
from typing import List
# class Solution:
    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     nums.sort()
    #     results = []
    #     n = len(nums)
    #     for i in range(n-3):
    #         a = nums[i]
    #         # 去重
    #         if i >= 1 and nums[i] == nums[i-1]:
    #             continue
    #         for j in range(i+1, n-2):
    #             b = nums[j]
    #             # 去重
    #             if j >= (i+2) and nums[j] == nums[j-1]:
    #                 continue
    #             right = n-1
    #             left = j+1
    #             while left < right:
    #                 sum = a+b+nums[right]+nums[left]
    #                 if sum > target:
    #                     right -= 1
    #                 elif sum < target:
    #                     left += 1
    #                 else:
    #                     results.append([a, b, nums[left], nums[right]])
    #                     # 去重
    #                     while left < right and nums[left] == nums[left+1]: left+=1 
    #                     while left < right and nums[right] == nums[right-1]: right-=1 
    #                     left +=1 
    #                     right -= 1
                    
    #     return results
    
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j >= (i+2) and nums[j] == nums[j-1]:
                    continue
                left_idx = j+1
                right_idx = len(nums) - 1
                while left_idx < right_idx:
                    sum = nums[left_idx] + nums[right_idx] + nums[i] + nums[j]
                    if sum == target:
                        result.append([nums[left_idx], nums[right_idx], nums[i], nums[j]])
                        while left_idx < right_idx and nums[left_idx] == nums[left_idx+1]: left_idx+=1 
                        while left_idx < right_idx and nums[right_idx] == nums[right_idx-1]: right_idx-=1 
                        left_idx += 1 
                        right_idx -= 1 
                    elif sum > target:
                        right_idx -= 1
                    else:
                        left_idx += 1
        return result
                
                
                
                
                
                
        
nums = [1,0,-1,0,-2,2]
target = 0 
s = Solution()
print(s.fourSum(nums, target))

                
        