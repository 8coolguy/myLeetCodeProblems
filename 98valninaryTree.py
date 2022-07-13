# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def left(root,l):
            if root and l:
                if root.val >l.val:
                    if not left(root, l.right): 
                        return False
                    if not left(root,l.left):
                        return False
                else:
                    return False
            return True
        def right(root,r):
            if root and r:
                if root.val < r.val:
                    if not right(root, r.right): 
                        return False
                    if not right(root,r.left):
                        return False
                    
                else:
                    print(root.val)
                    print(r.val)
                    return False
            return True
        def travel(root):
            if root:
                #
                if not left(root,root.left):
                    return False
                if not right(root,root.right):
                    return False
                if not travel(root.left):
                    return False
                if not travel(root.right):
                    return False
            return True
        return travel(root)
            
        