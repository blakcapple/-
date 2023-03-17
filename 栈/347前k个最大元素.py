# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

from typing import List
# 使用优先级队列数据结构
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 记录频率
        record = {} #nums[i]:对应出现的次数
        for i in range(len(nums)):
            record[nums[i]] = record.get(nums[i], 0) + 1
                
        priority_que = []
        for key, value in record.items():
            heapq.heappush(priority_que, (value, key))
        
            if len(priority_que) > k:
                heapq.heappop(priority_que)
            
        result = []
        for i in range(k):
            result.append(int(priority_que[i][1]))
        print(priority_que)
        result.reverse()
        
        return result
        
        
nums = [1,1,1,2,2,3]
k = 2
s = Solution()
print(s.topKFrequent(nums, k))