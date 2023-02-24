
# 给你二叉树的根节点 root ，返回它节点值的 后序 遍历。
# Definition for a binary tree node.
from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 把先序遍历的代码顺序变成中右左的遍历顺序，然后在反转result数组，输出的结果顺序就是左右中了
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        result.reverse()
        return result