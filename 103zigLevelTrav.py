# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#similar bfs to 101 and 102 which is pretty cool
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res=[]
        self.lt(root,0)
        return self.res
    def lt(self,root,l):
        if root:
            if len(self.res)<=l:
                self.res.append([])
            
            self.lt(root.right,l+1)
            self.lt(root.left,l+1)
            if (l+1)%2==0:
                self.res[l].append(root.val)
            else: self.res[l].insert(0,root.val)
            

