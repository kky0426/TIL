# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        queue=deque()
        while head:
            queue.append(head.val)
            head=head.next
        
        while len(queue)>1:
            if queue[0]!=queue[-1]:
                return False
            queue.pop()
            queue.popleft()
        return True
