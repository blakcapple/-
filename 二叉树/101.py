# 给你一个二叉树的根节点 root ， 检查它是否轴对称

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 利用递归函数对根节点的左右子树做遍历
        def compare(left_node, right_node):
            if left_node is None and right_node is None:
                return True 
            elif left_node is None and right_node is not None:
                return False 
            elif left_node is not None and right_node is None:
                return False
            elif left_node and right_node and (left_node.val!=right_node.val):
                return False
            # 最后剩下的一种情况为两个节点都为非空，且数值相等
            flag1 = compare(left_node.right, right_node.left)
            flag2 = compare(left_node.left, right_node.right)
            return flag1 and flag2
        return(compare(root.left, root.right))