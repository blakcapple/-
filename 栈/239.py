# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
# 你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

# 返回 滑动窗口中的最大值 。
from typing import List
from collections import deque
# 单调递减队列

class MyQue(object):
    
    def __init__(self):
        
        self.que = deque()
        
    def pop(self, value):
        
        if value == self.que[0]:
            self.que.popleft()
        
    def push(self, value):
        
        if self.que:
            while value > self.que[-1]:
                self.que.pop()
                if not self.que:
                    break
            self.que.append(value)
        else:
            self.que.append(value)
        
    def front(self):
        return self.que[0]
        
class Solution:
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        myque = MyQue()
        # 先将前k个值放到队列里面
        for i in range(k):
                myque.push(nums[i])
        # 记录最大值
        max_value = []
        max_value.append(myque.front())
        
        for i in range(k, len(nums)):
            myque.pop(nums[i-k])
            myque.push(nums[i])
            max_value.append(myque.front())
        return max_value
    
s = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(s.maxSlidingWindow(nums, k))