# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#similar to the other level traversal
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res =[]
        self.lt(root,0)
        return self.res
        
        
        
    def lt(self,root,l):
        if root:
            if len(self.res)-1 <l:
                self.res.append([])
            print(self.res)
            self.res[l].append(root.val)
            self.lt(root.left,l+1)
            self.lt(root.right,l+1)
