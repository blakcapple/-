# 给你一个字符串数组 tokens ，表示一个根据 逆波兰表示法 表示的算术表达式。

# 请你计算该表达式。返回一个表示表达式值的整数。

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == '+':
                a = stack.pop()
                b = stack.pop()
                c = int(a)+int(b)
                stack.append(c)
            elif s == '-':
                a = stack.pop()
                b = stack.pop()
                c = int(b)-int(a)
                stack.append(c)
            elif s == '/':
                a = stack.pop()
                b = stack.pop()
                c = int(b)/int(a)
                stack.append(c)
            elif s == '*':
                a = stack.pop()
                b = stack.pop()
                c = int(a)*int(b)
                stack.append(c)
            else:
                stack.append(s)
        return int(stack[-1])
    
s = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(s.evalRPN(tokens))