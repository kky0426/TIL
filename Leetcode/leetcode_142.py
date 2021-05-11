# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head==None:
            return None
        slow=head
        fast=head
        while True:
            if fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next
                if slow==fast:
                    break
            else:
                return None
            
            
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow
