count = 0
def quick_sort(arr):
    global count
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        # 根据选取的pivot值把数组分成左右两部分
        for i in arr[1:]:
            count += 1
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
        # 继续把左右两部分重复上面的步骤，最后返回拼接的数组
        return quick_sort(left) + [pivot] + quick_sort(right)
import numpy as np 
data = np.random.rand(10000)
sort_data = quick_sort(data)
print(count)

# 链表快排复杂度nlogn

class ListNode:
    
    def __init__(self, val=0, next=None):
        
        self.val = val
        self.next = next
    
def sortList(head: ListNode):
    
    if not head or not head.next:
        return head
    
    pivot = head 
    cur = head.next
    left = ListNode(0)
    right = ListNode(0)
    l = left 
    r = right
    # 分成两部分
    while cur:
        if cur.val < pivot.val:
            l.next = cur
            l = l.next
        else:
            r.next = cur 
            r = r.next
        cur = cur.next 
    l.next = None
    r.next = None
    # 对左右部分都进行快排
    left = sortList(left.next)
    right = sortList(right.next)
    # 拼接
    pivot.next = right
    left = append(left, pivot)
    return left
    
def append(left, pivot):
    # 拼接
    if not left:
        return pivot
    cur = left 
    while cur.next:
        cur = cur.next
        
    cur.next = pivot
    
    return left 

# head = ListNode(10)
# cur = head 
# for i in range(100,0,-1):
#     cur.next = ListNode(i)
#     cur = cur.next
# new_head = sortList(head)
# cur = new_head
# while cur:
#     print(cur.val)
#     cur = cur.next
head = ListNode(10)
cur = head # cur 和 head 指向同一个地址，只有单个的值才是赋值
cur.next = ListNode(1) # 改变cur会同时改变head
print(head.next.val)