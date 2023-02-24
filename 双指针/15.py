##给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
# 同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
#你返回所有和为 0 且不重复的三元组。
from typing import List
class Solution:
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        # 先对数组做排序（升序）
        nums.sort()
        num_len = len(nums)
        results = []
        # 利用双指针寻找三元组
        for i in range(num_len-2):
            a = nums[i]
            left = i+1 
            right = num_len-1
            # 去重第一个元素
            if i>=1 and nums[i] == nums[i-1]:
                continue
            while left < right:
                # 大于零，则右指针要向左移
                if a + nums[left] + nums[right] > 0:
                    right -= 1
                # 小于零，则左指针要向有移动
                elif a + nums[left] + nums[right] < 0:
                    left +=1 
                else: 
                    results.append([a, nums[left], nums[right]])
                    # 防止后面的元素重复
                    while left < right and nums[right] == nums[right-1]: right -=1 
                    while left < right and nums[left] == nums[left+1]: left += 1 
                    left += 1
                    right = right-1
                    
        return results
    
nums = [-1,0,1,2,-1,-4]

results = Solution.threeSum(nums)    
print(results)   
        
        
        