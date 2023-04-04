# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

# 有效 二叉搜索树定义如下：

# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.pre = None
        def backtrack(root):
            if not root:
                return True
            # 中序遍历
            left = backtrack(root.left)
            if self.pre and (self.pre.val >= root.val): return False
            self.pre = root
            right = backtrack(root.right)
            return left and right
         
        flag = backtrack(root)
        return flag
    
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)

s = Solution()
print(s.isValidBST(root))
