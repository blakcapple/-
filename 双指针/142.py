# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
# 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

# 不允许修改 链表。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 快慢指针法 快指针去追赶慢指针;如果是环就能追上
        if not head:
            return None
        slow_idx = head
        fast_idx = head
        flag = False
        while slow_idx.next and fast_idx.next and fast_idx.next.next:
            if slow_idx.next == fast_idx.next.next:
                node = slow_idx.next # 环内相遇节点
                flag = True
                break
            slow_idx = slow_idx.next
            fast_idx = fast_idx.next.next
        if not flag:
            return None
        cur1 = head
        cur2 = node
        if cur1 == cur2:
            return cur1
        while head.next:
            if cur1.next == cur2.next:
                return cur1.next
                break
            cur1 = cur1.next
            cur2 = cur2.next
        
        