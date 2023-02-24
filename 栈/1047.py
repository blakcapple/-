class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for item in s:
            if not stack:
                stack.append(item)
            elif item == stack[-1]:
                stack.pop()
            else:
                stack.append(item)
        return ''.join(stack)
    
s1 = Solution()
s = "abbaca"
print(s1.removeDuplicates(s))