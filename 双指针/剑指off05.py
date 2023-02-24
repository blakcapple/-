# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

class Solution:
    def replaceSpace(self, s: str) -> str:
        
        # 首先扩充字符串
        count = s.count(' ')
        s = list(s)
        idx1 = len(s) - 1 
        s.extend([''] * count*2)
        # 从后往前遍历
        idx2 = len(s) - 1
        while idx1 >= 0:
            if s[idx1] != ' ':
                s[idx2] = s[idx1]
                idx2 -= 1
            else:
                s[idx2] = '0'
                s[idx2-1] = '2'
                s[idx2-2] = '%'
                idx2 -= 3
            idx1 -=1 
        return ''.join(s)
    
s1 = Solution()
s = "We are happy."
print(s1.replaceSpace(s))