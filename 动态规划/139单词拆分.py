#给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

#注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
from typing import List
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         dp = [False] * (len(s)+1)
#         dp[0] = True
#         for i in range(1,len(s)+1):
#             for word in wordDict:
#                 if len(word) > i:
#                     continue
#                 else:
#                     if dp[i-len(word)] is True and s[i-len(word):i] == word:
#                         dp[i] = True 
#         print(dp)
#         return dp[-1]
    
# s1 = Solution()
# s = "leetcode"
# wordDict = ["leet", "code"]
# print(s1.wordBreak(s, wordDict))

def wordBreak(s: str, wordDict: List[str]):

    dp = [False for _ in range(len(s)+1)]
    dp[0] = True
    for item in wordDict:
        for size in range(len(item), len(s)+1):
            if dp[size-len(item)] == True and s[size-len(item):size] == item:
                dp[size] = True
    print(dp)
s = "leetcode"
wordDict = ["leet", "code"]
wordBreak(s, wordDict)
