#Leetcode Problems:

# 876. Middle of the Linked List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def middleNode(head: ListNode | None) -> ListNode | None:
    count=0
    curr=head
    while curr:
        count +=1
        curr=curr.next
    mid=count//2

    curr=head
    for i in range(mid):
        curr=curr.next
    return curr
n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
result = middleNode(n1)
print(result.val)  

#Another approach using slow and fast pointers
''' slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow
            '''

# 141. Linked List Cycle

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited=set()
        curr=head
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr=curr.next
        return False
    #True Case
x = ListNode(1)
y = ListNode(2)
z = ListNode(3)
x.next = y
y.next = z
z.next = x
print(Solution().hasCycle(x)) 
    #False case
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
print(Solution().hasCycle(a)) 

#Another approach using slow and fast pointers
''' slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
        return False'''

# 19. Remove Nth Node From End of List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        count=0
        curr=head
        while curr:
            count +=1
            curr=curr.next
        dummy=ListNode()
        dummy.next=head
        curr=dummy
        for i in range(count-n):
            curr=curr.next
        curr.next=curr.next.next
        return dummy.next
# 21. Merge Two Sorted Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        new_node=ListNode()
        curr=new_node
        while list1 and list2:
            if list1.val<=list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next
        if list1:
            curr.next=list1
        else:
            curr.next=list2
        return new_node.next
