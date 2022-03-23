#made the solution on my own
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        #3 cases start > target
            #return start - target
        #2 target> start
        
        #1 target==start
            #return 0
        print(target)
        if startValue == target:
            return 0
        if startValue > target:
            return startValue-target
        if target >startValue:
            if target%2==1:
                return 1+self.brokenCalc(startValue,target+1)
            else:
                return 1+self.brokenCalc(startValue,target//2)
            
        #notes on greedy solution
        #optimization problem get min/max
        