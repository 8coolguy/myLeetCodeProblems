#had to look up solution but i think I got a hang of it
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result =nums[0]+nums[1] +nums[2]
        #go through the array for the first one 
        for i in range(len(nums)-2):
            
            j=i+1
            k=len(nums)-1
            #use 2 pointers search for the other 2 numbers
            while k > j:
                tot =nums[i]+nums[j] +nums[k]
                if tot ==target:
                    return tot
                
                
                if abs(tot - target) < abs(result - target):
                    result = tot
                #move the ptrs if the tot is not less
                if tot < target:
                    j += 1
                elif tot > target:
                    k -= 1
        
        
        
        
        
        
        
        return result
        
