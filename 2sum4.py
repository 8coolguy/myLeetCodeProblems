# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#i want to check for faster solutions
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def traversal(leaf,root):
            if leaf.left != None:
                if search(leaf.left.val,root):
                    return True
            if leaf.right != None:
                if search(leaf.right.val,root):
                    return True
            if leaf.left != None:
                if traversal(leaf.left,root):
                    return True
            if leaf.right != None:
                if traversal(leaf.right,root):
                    return True
        
        def search(leaf_val,root):
            if root !=None:
                if leaf_val != root.val:
                    target =root.val+leaf_val
                    if target >k:
                        if root.left !=None:
                            if search(leaf_val,root.left):
                                return True
                        else: 
                            return False
                    elif target< k:
                        if root.right !=None:
                            if search(leaf_val,root.right):
                                return True
                        else:
                            return False
                    else:
                        return True
                else:
                    return search(leaf_val,root.left) or search(leaf_val,root.right)
            return False
                    
                    
                    
                    
        
        if root.val !=None:
            if search(root.val,root):
                return True
            if traversal(root,root):
                return True
        return False
            
        
