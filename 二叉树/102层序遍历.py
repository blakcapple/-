# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
from typing import Optional,List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque()
        que.append(root)
        results = []
        # 核心思想 dfs
        while que:
            result = []
            size = len(que)
            # 一层一层遍历
            for i in range(size):
                node = que.popleft()
                if not node:
                    break
                result.append(node.val)
                if node.left:que.append(node.left)
                if node.right:que.append(node.right)
            results.append(result)
        return results
        