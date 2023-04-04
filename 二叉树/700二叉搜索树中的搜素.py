# 给定二叉搜索树（BST）的根节点 root 和一个整数值 val。

# 你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
# 递归法
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def backtracking(node):
            if not node:
                return None 
            if node.val > val:
                backtracking(node.left)
            elif node.val < val:
                backtracking(node.right)
            else:
                return node
        backtracking(root)
# 迭代法
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None:
            if val < root.val: root = root.left
            elif val > root.val: root = root.right
            else: return root
        return None
    

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.result = None
        def backtrack(node):
            if not node:
                return 
            if node.val == val:
                self.result = node
            if node.val > val:
                backtrack(node.left)
            if node.val < val:
                backtrack(node.right)
        
        backtrack(root)
        return self.result
    

s = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(s.searchBST(root, 1))

        