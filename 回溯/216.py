# 找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：

# 只使用数字1到9
# 每个数字 最多使用一次 
# 返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(k, StartIndex):
            if len(path) == k and sum(path) == n:
                res.append(path[:])
                return
            for i in range(StartIndex, 9 + 1): # 横向遍历
                path.append(i)
                backtrack(k, i+1) # 纵向遍历
                path.pop()
        backtrack(k, 1)
        return res
    
k = 3
n = 9
s = Solution()
print(s.combinationSum3(k,n))
        