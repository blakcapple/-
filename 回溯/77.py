# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

# 你可以按 任何顺序 返回答案。
from typing import List
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         res = []
#         path = []
#         def backtrack(n, k, StartIndex):
#             if len(path) == k:
#                 res.append(path[:])
#                 return
#             for i in range(StartIndex, n + 1): # 横向遍历
#                 path.append(i)
#                 backtrack(n, k, i+1) # 纵向遍历
#                 path.pop()
#         backtrack(n, k, 1)
#         return res

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:  
        path = []
        results = []
        def help(n, start_idx):
            if len(path) == k:
                results.append(path[:]) # 注意列表的引用性质
                return 
            for i in range(start_idx, n+1):
                path.append(i)
                help(n, i+1)
                path.pop()
        help(n, 1)
        return results
    
                    
                
n = 3 
k = 2
s = Solution()
print(s.combine(n,k))