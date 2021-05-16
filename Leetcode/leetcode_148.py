# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def merge(left,right):
        head=ListNode()
        cur=head
        while left and right:
            if left.val<right.val:
                cur.next=left
                left=left.next
                cur=cur.next
            else:
                cur.next=right
                right=right.next
                cur=cur.next
        if left:
            cur.next=left
        else:
            cur.next=right
        
        return head.next
         
    def mergesort(head):
        if not head or not head.next:
            return head
        mid,slow,fast=None,head,head
        while fast and fast.next:
            mid=slow
            slow=slow.next
            fast=fast.next.next
        mid.next=None
        
        left=self.mergesort(head)
        right=self.mergesort(slow)
        
        return self.merge(left,right)
        
    def sortList(self, head: ListNode) -> ListNode:
        
        def merge(left,right):
            head=ListNode()
            cur=head
            while left and right:
                if left.val<right.val:
                    cur.next=left
                    left=left.next
                    cur=cur.next
                else:
                    cur.next=right
                    right=right.next
                    cur=cur.next
            if left:
                cur.next=left
            else:
                cur.next=right
        
            return head.next
        
        def mergesort(head):
            if not head or not head.next:
                return head
            mid,slow,fast=None,head,head
            while fast and fast.next:
                mid=slow
                slow=slow.next
                fast=fast.next.next
            mid.next=None
        
            left=mergesort(head)
            right=mergesort(slow)
        
            return merge(left,right)
    
        return mergesort(head)
