"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        chead=head
        while chead:
            node=Node(chead.val)
            node.random=chead.random
            node.next=chead.next
            chead.next=node
            chead=node.next
        
        chead=head
        while chead:
            if chead.next.random:
                chead.next.random=chead.random.next
            chead=chead.next.next
        
        
        chead=head.next
        while chead and chead.next:
            chead.next=chead.next.next
            chead=chead.next
        return head.next
            
