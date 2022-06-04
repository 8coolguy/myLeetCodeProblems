#got it done
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source ==destination:
            return True
        v=(n)*[False]
        d=defaultdict(list)
        for i in edges:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
            
        def travel(node,edges,v,d):
            if v[node]:
                return False
            if node ==d:
                return True
            v[node]=True
            for i in edges[node]:
                if travel(i,edges,v,d): return True 
            return False
        return travel(source,d,v,destination)
                                                                                                   
        