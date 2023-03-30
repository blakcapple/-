# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
# Definition for a binary tree node.
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 递归法        
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 递归法 dfs 深度优先搜索
        result = []
        def traversal(node, result):
            if node == None:
                return 
            result.append(node.val)
            traversal(node.left, result)
            traversal(node.right, result)
        traversal(root, result)
        return result
# 迭代法（利用栈的结构）
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        reslut = []
        stack = [root]
        while stack:
            node = stack.pop()
            reslut.append(node.val)
            if node.right:stack.append(node.right)
            if node.left: stack.append(node.left)
        return reslut
    
    