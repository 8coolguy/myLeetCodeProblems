
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#not my solution but kinda understand the bfs solution
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q=[root]#create a q
        while q:#while there is stuff in the q
            curr=q.pop()#get first ele
            if curr.left and curr.right:    #if 2 children
                curr.left.next = curr.right#set the next to the right
                if curr.next:#if tthere is a next of the curr then set the right next to the left of that
                    curr.right.next = curr.next.left
               
                q.append(curr.left)#sadd to q
                q.append(curr.right)
        return root
            
