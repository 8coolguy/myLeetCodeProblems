# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#im definetly improving
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(r):
            if r:
                return 1+max(height(r.left),height(r.right))
            else:
                return 0
        def travel(root,m):
            if root:
                t=height(root.right)+height(root.left)
                if t >m:
                    m=t
                return max(travel(root.right,m),travel(root.left,m))
            return m
        return travel(root,0)
        
