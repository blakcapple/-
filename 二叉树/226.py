# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
# Definition for a binary tree node.
from typing import Optional,List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        que = deque()
        que.append(root)
        while que:
            size = len(que)
            for i in range(size):
                node = que.popleft()
                if not node:
                    break
                node.right, node.left = node.left, node.right
                if node.left:que.append(node.left)
                if node.right:que.append(node.right)
        return root