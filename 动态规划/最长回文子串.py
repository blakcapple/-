# 给你一个字符串 s，找到 s 中最长的回文子串。

# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
# 暴力循环（会超时）
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_count = 0
        start = 0 
        end = 1
        # if len(s) == 1:
        #     return s
        # if len(s) == 2:
        #     if s[0] == s[1]:
        #         return s 
        #     else:
        #         return s[0]
        def check(input):
            left_idx = 0
            right_idx = len(input) - 1 
            while (left_idx < right_idx):
                if input[left_idx] != input[right_idx]:
                    return False 
                left_idx += 1
                right_idx -= 1
            return True 
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if check(s[i:j]):
                    count = j - i 
                    if count > max_count:
                        max_count = count
                        start = i 
                        end = j
        return s[start:end]

# 动态规划
import numpy as np
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        # dp[i][j] 表示以索引i开始，j结束的字符串是否是回文串
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        start = 0 
        end = 0+max_len
        # 长度为1的必然是回文串
        for i in range(n):
            dp[i][i] = True
        # 枚举子串长度
        for L in range(2, n+1):
            # 枚举左边界
            for left_idx in range(0, n):
                # 右边界可以计算得到
                right_idx = L+left_idx-1
                if right_idx >= n:
                    break
                if s[right_idx] != s[left_idx]:
                    dp[left_idx][right_idx] = False
                else:
                    # 如果边界相等，则是否是回文串取决于去掉边界后的字符串
                    if L < 3:
                        dp[left_idx][right_idx] = True
                    else:
                        dp[left_idx][right_idx] = dp[left_idx+1][right_idx-1]
                if dp[left_idx][right_idx] and L > max_len:
                    max_len = L 
                    start = left_idx
                    end = right_idx + 1
        return s[start:end]
                            
s = "aacabdkacaa"
s1 = Solution()
print(s1.longestPalindrome(s))


