# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l=0
        temp=head
        while temp:
            l+=1
            temp=temp.next
      
       
        count=0
        cur=head
        front=cur
        if l-n == 0:
            return head.next
        
        while head:
            if count == l-n:
                front.next=head.next
                break
            else:
                front=head
                head=head.next
                count+=1
        return cur
