# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode(0)
        cur=head
        carry=0
        front=None
        x,y=0,0
        while l1 or l2:
            if l1:
                x=l1.val
            else:
                x=0
            if l2:
                y=l2.val
            else:
                y=0
            s=x+y+carry
            if s>=10:
                carry=s//10
                s=s%10
            else:
                carry=0
            node=ListNode(s)
            cur.next=node
            cur=cur.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        
        if carry>0:
            node=ListNode(carry)
            cur.next=node
            
        
        return head.next
            
