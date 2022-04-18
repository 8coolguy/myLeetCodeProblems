#4sum on my own by recalling 3 sum i think run time is like of O cubed or quad or smth
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def areUnique(nums,res):
            my_set=set(nums)
            for i in res:
                if set(i) ==my_set:
                    return False
            return True
        
        nums.sort()
        res=[]
        n=len(nums)
        for i in range(n-3):
            for j in range(i+1,n-2):
                k=j+1
                l=n-1
                while l>k:
                    if nums[i]+nums[j]+nums[k]+nums[l] ==target  and areUnique([nums[i],nums[j],nums[k],nums[l]],res) :
                        res.append([nums[i],nums[j],nums[k],nums[l]])
                        
                    elif nums[i]+nums[j]+nums[k]+nums[l] >target:
                        l-=1
                    else:
                        k+=1
        return res
    
       
