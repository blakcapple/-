from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

def maxDepth(root: Optional[TreeNode]) -> int:
    def backtrack(node):
            global max_length # 全局变量声明 为声明path不用声明，但是max_length需要声明
            if not node:
                length = len(path)
                if length > max_length:
                    max_length = length
                return 
            path.append(node)
            backtrack(node.left)
            backtrack(node.right)
            path.pop()
    if not root:
        return 0 
    path = []
    global max_length
    max_length = 0
    backtrack(root)
    return max_length

root = TreeNode(10)
root.left = TreeNode(10)

print(maxDepth(root))