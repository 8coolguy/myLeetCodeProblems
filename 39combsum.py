
#not my solution but ths is an example of back tracking i need to learnmore of this thing 
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #i guess we need to do some backtracking or smthng
        
        def backTrack(target,arr,k):
            
            if (target == 0):
                #this is for when it has reached the target
                self.sol.append(arr)
            if(target <0 or k >=len(candidates)):
                return
            for i in range(k, len(candidates)):
                backTrack(target-candidates[i],arr+[candidates[i]],i)
        candidates.sort()
        self.sol=[]
        
        backTrack(target,[],0)        
        return self.sol
                
