# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        count = 0
        # 定义两个指针
        left_node = ListNode(next=head)
        right_node = ListNode(next=head)
        tmp = left_node
        for i in range(n):
            right_node = right_node.next
        while right_node.next:
            left_node = left_node.next
            right_node = right_node.next
        left_node.next = left_node.next.next
        
        return tmp.next 
                            