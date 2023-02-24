# 给你二叉树的根节点 root ，返回它节点值的 中序 遍历。
# Definition for a binary tree node.
from typing import Optional,List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 迭代法
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 逻辑：不断地把左子树的节点压到栈中；一直访问到叶节点后，把节点挤出栈，然后压入右字数的节点，循环往复
        if not root:
            return []
        stack = []
        result = []
        cur = root 
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
                
        return result