# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        #true if subpath equals the linked list
        #false if it doesn't
        
        def compare(root,head):
            if root!=None and head!=None:
                if head.val== root.val:
                    return compare(root.left,head.next) or compare(root.right, head.next)
                else:
                    return compare(root.left,head) or compare(root.right, head)
            elif head==None:
                return True
            else:
                return False
        if not head: return True
        if not root: return False
        return compare(root,head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)