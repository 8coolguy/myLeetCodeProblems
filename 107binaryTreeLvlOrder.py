# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass
        self.res =[]
        self.lT(root,0)
        return self.res
        
    def lT(self,root,l):
        if not root:
            return
        else:
            if len(self.res)-1 <l:
                self.res.insert(0,[])
            self.lT(root.left,l+1)    
            self.lT(root.right,l+1)
            self.res[len(self.res)-l-1].append(root.val)
                
        
        
