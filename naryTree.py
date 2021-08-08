#this was fairly simple nust got to go throught the tree and return an array for all the depth
#i used some reucursion adn got er thing done
#wrote a useless get depth function too
#time was kinda slow too
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def getDepth(root):
        if root ==None:
            return 1
        maxDepth =0
        for child in root.children:
            d =Solution.getDepth(child)
            if d>maxDepth:
                maxDepth =d
        return maxDepth+1
    def lookThru(arr,root,i):
        arr.append([])
        for child in root.children:
            arr[i].append(child.val)
            if len(child.children) >0:
                Solution.lookThru(arr,child,i+1)
        if len(arr[-1]) ==0:
            arr.pop()


    def levelOrder(self, root: 'Node') -> List[List[int]]:
        #d=Solution.getDepth(root)
        ans=[[]]
        if root != None:
            ans[0].append(root.val)
        else:
            return []

        Solution.lookThru(ans,root,1)
        return ans



