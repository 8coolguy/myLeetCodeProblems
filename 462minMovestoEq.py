#ayy les make this streak go crazy
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        c=0
        m=(l+r)//2
        while(r>l):
            c+=nums[m]-nums[l]
            c+=nums[r]-nums[m]
            r-=1
            l+=1
        return c
                
        