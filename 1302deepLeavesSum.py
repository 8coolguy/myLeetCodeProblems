# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#well okay ill take that came out of nowhere but i got this babey
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        #find height of tree
        #if height =root height add to total
        def height(root):
            if root !=None:
                return 1+max(height(root.left),height(root.right))
            else:
                return 0

    
        def traverse(rt,tot,h):
            if rt != None:
                if rt.left==None and rt.right==None and h==1:
                    return tot+rt.val
                else:
                    tot+=traverse(rt.left,0,h-1)
                    tot+=traverse(rt.right,0,h-1)
                    print(tot)
                    return tot
            return 0

        return traverse(root,0,height(root))
        
                
        