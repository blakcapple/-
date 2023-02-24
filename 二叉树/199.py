# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional,List
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 在层次遍历的基础上判断是否是每一层的最后一个元素即可
        if not root:
            return []
        que = deque()
        que.append(root)
        results = []
        while que:
            size = len(que)
            for i in range(size):
                node = que.popleft()
                if not node:
                    break
                if i == (size -1):
                    results.append(node.val)
                if node.left:que.append(node.left)
                if node.right:que.append(node.right)
        return results