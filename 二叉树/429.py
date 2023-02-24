"""
给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。

树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

"""
from typing import Optional,List
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        que = deque()
        que.append(root)
        results = []
        while que:
            result = []
            size = len(que)
            for i in range(size):
                node = que.popleft()
                if not node:
                    break
                result.append(node.val)
                for next in node.children:
                    que.append(next)
            results.append(result)
        return results