# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

from typing import List
def letterCombinations(digits: str) -> List[str]:
    if len(digits)==0:
        return ['']
    number_map = {1:'', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
    result = []
    path = []
    def backtrack(index):
        # 返回
        if index >= len(digits):
            
            result.append(''.join(path[:]))
            return 
            
        # 横向遍历
        for item in number_map[int(digits[index])]:
            path.append(item)
            backtrack(index+1)
            path.pop()
    backtrack(0)
    return result
digits = "23"
print(letterCombinations(digits))