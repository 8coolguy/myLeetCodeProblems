
#not my solution but it seems to work on this prolems tho 
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
       
        start = len(gas)-1
        end =0
        total = gas[start]-cost[start]
        
        while(start>end):
            # you can move forward because it the gas is greater than the cost 
            if(total >= 0):
                total+=gas[end]-cost[end]
                end+=1
            #in this situation you have to move back because you cant complete circuit
            else:
                start-=1
                total+=gas[start]-cost[start]
        if(total>=0):
            return start
        else:
            return -1
