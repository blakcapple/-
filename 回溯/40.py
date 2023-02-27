#给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的每个数字在每个组合中只能使用一次。

# 说明： 所有数字（包括目标数）都是正整数。解集不能包含重复的组合。
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        path_sum = 0
        candidates.sort()
        def help(start_idx, path_sum, target, used):
            if path_sum >= target:
                if path_sum == target:
                    res.append(path[:])
                return 
            for i in range(start_idx, len(candidates)):
                if i >= 1 and candidates[i] == candidates[i-1] and used[i-1] == False: # 只对同一树层的去重
                    continue
                path.append(candidates[i])
                path_sum += candidates[i]
                used[i] = True # True 说明进入纵向递归
                help(i+1, path_sum, target, used)
                used[i] = False # False 说明进入横向遍历
                path.pop()
                path_sum -= candidates[i]
        used = [False] * len(candidates)
        help(0, path_sum, target, used)
        return res
s = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(s.combinationSum2(candidates, target))