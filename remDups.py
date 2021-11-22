class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        if(len(nums)<=1):
            return
        #while(len(nums)-1!=i):
            #print(nums[i])
        #    if(nums[i]==nums[i+1]):
        #        nums.pop(i)
        #        continue
        #    i+=1
        nums[:] = sorted(set(nums))
        return len(nums)
        #nums=list(set(nums)).copy()
        
            
        
