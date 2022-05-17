# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#thats all me boi...
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def rec(r,h):
            if r:
                if not r.left and not r.right:
                    return h
                else:
                    return min(rec(r.left,h), rec(r.right,h))+1
            else:
                return float('inf')
        return rec(root,1)
            
