# 给你一个字符串 s ，请你反转字符串中 单词 的顺序。

# 单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。

# 返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。

# 注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

class Solution:
    def reverseWords(self, s: str) -> str:
        # 去除多余的空格
        def erasespace(input):
            left_idx  = 0 
            tmp = []
            right_idx = len(input) - 1
            while left_idx <= right_idx:
                if input[left_idx] == ' ':
                    left_idx +=1 
                else:
                    break
            while left_idx <= right_idx:
                if input[right_idx] == ' ':
                    right_idx -=1
                else:
                    break
            for i in range(left_idx, right_idx+1):
                if i == 0:
                    tmp.append(input[i])
                elif input[i] != ' ':
                    tmp.append(input[i])
                elif input[i-1] != ' ':
                    tmp.append(input[i])
            return tmp
        
        def reverse(input):
        # 翻转字符串
            left_idx = 0 
            right_idx = len(input) - 1
            while left_idx <= right_idx:
                input[left_idx], input[right_idx] = input[right_idx], input[left_idx]
                left_idx += 1
                right_idx -= 1
                
        def reverse_world(input):
            # 翻转字符
            left_idx = 0 
            right_idx = 0
            while right_idx < len(input):
                while right_idx<len(input) and input[right_idx] != ' ':
                    right_idx += 1
                tmp_idx = right_idx - 1
                while left_idx <= tmp_idx:
                    input[left_idx], input[tmp_idx] = input[tmp_idx], input[left_idx]
                    left_idx += 1
                    tmp_idx -= 1
                right_idx += 1
                left_idx = right_idx
        
        result = erasespace(s)
        reverse(result)
        reverse_world(result)
        return ''.join(result)