class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
       
        
        self.v=[0]*numCourses#keeps tracks of all the nodes visited
        self.graph = collections.defaultdict(list)#graph stores all edges of the graph from prequeists default dict so it can store multiple requistes
        for pair in prerequisites:
            self.graph[pair[0]].append(pair[1])
        self.res=[]#stores all the results of the search
        for i in range(numCourses):#goes through each course
            if not self.dfs(i):
                return []
        return self.res
        
        
    def dfs(self,node):
        if self.v[node]==-1:#if the visited node is False just leave 
            return False
        if self.v[node]==1:#if already visited and true
            return True
        self.v[node]=-1
        #go through graph nodes to find other ones
        for i in self.graph[node]:
            if not self.dfs(i):
                return False
        self.res.append(node)    
        self.v[node]=1
        return True
        
       
