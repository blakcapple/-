# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。
# 判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。
# 如果存在，返回 true ；否则，返回 false 。

# 叶子节点 是指没有子节点的节点。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List

class Solution:
    def hasPathSum(self, root: Optional[TreeNode],targetSum: int) -> List[str]:
        self.flag = False
        result = []
        path = []
        def backtrack(node):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                path_sum = sum(path)
                if path_sum == targetSum:
                    self.flag = True 
            backtrack(node.left)
            backtrack(node.right)
            path.pop()
            
        backtrack(root)
        return self.flag
    
    
root = TreeNode(1)
root.left = TreeNode(2)
s = Solution()
print(s.hasPathSum(root, 1))




