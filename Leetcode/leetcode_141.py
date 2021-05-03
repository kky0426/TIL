# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        p1=head
        p2=head.next
        while p1!=p2:
            if p2==None or p2.next==None:
                return False
            p1=p1.next
            p2=p2.next.next
            
        return True
        
