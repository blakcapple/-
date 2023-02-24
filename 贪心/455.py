# 假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。

# 对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。
# 如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 对饼干和胃口进行排序，大饼干首先满足大胃口
        s.sort()
        g.sort()
        result = 0
        index = len(s)-1
        if index < 0:
            return result
        for i in range(len(g)-1, -1, -1):
            if s[index] >= g[i] and index >= 0: 
                index -= 1
                result += 1
                if index < 0:
                    break
        return result
    
s1 = Solution()
g = [10,9,8,7]
s = [5,6,7,8]
print(s1.findContentChildren(g, s))