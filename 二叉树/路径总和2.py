# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

# 叶子节点 是指没有子节点的节点。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List

class Solution:
    def pathSum(self, root: Optional[TreeNode],targetSum: int) -> List[str]:
        result = []
        path = []
        def backtrack(node):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                path_sum = sum(path)
                if path_sum == targetSum:
                    result.append(path[:])
            backtrack(node.left)
            backtrack(node.right)
            path.pop()
            
        backtrack(root)
        return result
    
    
root = TreeNode(1)
root.left = TreeNode(2)
s = Solution()
print(s.PathSum(root, 3))
