# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

# 回文串 是正着读和反着读都一样的字符串。
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(input):
            right_idx = len(input) - 1 
            left_idx = 0
            while left_idx <= right_idx:
                if input[left_idx] != input[right_idx]:
                    return False
                left_idx += 1
                right_idx -= 1
            return True 
        
        path = []
        results = []
        def backtracking(start_idx):
            if start_idx >= len(s):
                results.append(path[:])
                return 
            for i in range(start_idx, len(s)):
                # 判断是否是回文串:
                if check(s[start_idx:i+1]):
                    path.append(s[start_idx:i+1])
                else:
                    continue
                backtracking(i+1)
                path.pop()
        backtracking(0)
        return results
s1 = Solution()
s = "aab" 
print(s1.partition(s))

                
            
            
            