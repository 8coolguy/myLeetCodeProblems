# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#got 2 for the day this was an easy one because you just had to toraverse
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        def traverse(root,arr):
            if(root!=None):
                #print(root.val)
                x=traverse(root.left,arr)
                y=traverse(root.right,arr)
                if(x and y ):
                    arr.append(root.val)
                return False
            else:
                return True
        res1=[]
        res2=[]
        traverse(root1,res1)
        traverse(root2,res2)
        if len(res1)!=len(res2):
            return False
        for i in range(len(res1)):
            if res1[i]!=res2[i]:
                return False
        return True
            
        