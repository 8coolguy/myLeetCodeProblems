#another problem
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        res=[-1,-1]
        l=0
        h=len(nums)-1
        while h >= l:
            print(h)
            print(l)
            if nums[h] ==target:
                res[-1]=h
                if res[0] != -1 and res[-1] !=-1 and nums[res[0]] ==target and nums[res[-1]] ==target:
                    break
            else:
                h-=1
            if nums[l] ==target:
                res[0] = l
                if res[0] != -1 and res[-1] !=-1 and nums[res[0]] ==target and nums[res[-1]] ==target:
                    break
            else:
                l+=1
            print("end")
            
                
        
        
        return res
        