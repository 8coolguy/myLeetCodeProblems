#not my solution but i understand it uses a bfs to eleiminate rtreees toll it has the 2 nodes that maek the min tree

#breadth
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if edges==[]:
            return [0]
        
        my_dict=defaultdict(set)
        visited =[False]*n
     

        #make an undirected tree
        for u,v in edges:
            my_dict[u].add(v)
            my_dict[v].add(u)
            
        print(my_dict)
        leaves=[]
        new_leaves=[]
        in_degree=[]
        
        for i in range(n):
            if len(my_dict[i])==1:
                leaves.append(i)
            in_degree.append(len(my_dict[i]))
        while n >2:
            for leaf in leaves:
                for adj in my_dict[leaf]:
                    in_degree[adj] -=1
                    if in_degree[adj] ==1:
                        new_leaves.append(adj)
            n-=len(leaves)
            leaves=new_leaves[:]
            new_leaves =[]
            
        return leaves
        
        
        
    