# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

# 图示两个链表在节点 c1 开始相交：

# 题目数据 保证 整个链式结构中不存在环。

# 注意，函数返回结果后，链表必须 保持其原始结构 。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        # 计算两个链表的差值
        countA = 0
        countB = 0
        if not headA or not headB:
            return None
        node = headA
        while node.next:
            node = node.next
            countA += 1
        node = headB
        while node.next:
            node = node.next
            countB += 1
        dif = countA - countB
        nodeA = headA
        nodeB = headB
        if dif > 0:
            for i in range(dif):            
                nodeA = nodeA.next
        else:
            for i in range(-dif):            
                nodeA = nodeA.next
        while nodeB:
            if nodeB == nodeA:
                return nodeA
            nodeB = nodeB.next
            nodeA = nodeA.next 
        return None
            