"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#i really need to take the time and understand these problems through and through need to do no solution sundays???
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q=[root]
        while q:
            c=q.pop(0)
            nq=[]
            while c:
                if q:
                    c.next=q.pop(0)
                else:
                    c.next=None
                if c.left: nq.append(c.left)
                if c.right: nq.append(c.right)
                c=c.next
            q=nq
        return root
                
        
