# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。

# 叶子节点 是指没有子节点的节点。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        result = []
        path = []
        def backtrack(node):
            if not node:
                return
            path.append(f'{node.val}')
            if not node.left and not node.right:
                result.append('->'.join(path))
                
            backtrack(node.left)
            backtrack(node.right)
            path.pop()
            
        backtrack(root)
        return result
    
root = TreeNode(1)
root.left = TreeNode(2)
s = Solution()
print(s.binaryTreePaths(root))