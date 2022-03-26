# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #you have to compare the left of left with right of right and so on
        def symCheck(rootL,rootR):
            if not rootL and not rootR:
                return True
            if rootL and rootR and rootL.val==rootR.val:
                return symCheck(rootL.right,rootR.left) and symCheck(rootR.right,rootL.left)
            return False
        #dont need to check if root is NULL because range og nodes starts at 1 so we knwo there will alwasy be a root
        return symCheck(root.left, root.right)
        
       