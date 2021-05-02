# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        count_a=0
        count_b=0
        n1=headA
        n2=headB
        while n1:
            n1=n1.next
            count_a+=1
        while n2:
            n2=n2.next
            count_b+=1
        diff=count_a-count_b
        if diff<0:
            for i in range(abs(diff)):
                headB=headB.next
        else:
            for i in range(diff):
                headA=headA.next
                
        while headA:
            if headA==headB:
                return headA
            else:
                headA=headA.next
                headB=headB.next
        return None
        
