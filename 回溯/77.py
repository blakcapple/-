# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

# 你可以按 任何顺序 返回答案。
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(n, k, StartIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(StartIndex, n + 1): # 横向遍历
                path.append(i)
                backtrack(n, k, i+1) # 纵向遍历
                path.pop()
        backtrack(n, k, 1)
        return res
    
n = 3 
k = 2
s = Solution()
s.combine(n,k)