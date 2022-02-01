#not my solution but worked and understood wacthceh this videoi
#https://www.youtube.com/watch?v=DKCbsiDBN6c
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def BackTrack(s,e):
            if(s==e):
                
                self.perms.append(nums[:])
                #print(self.perms)
                
            for i in range(s,e):
                #print(nums)
                nums[s],nums[i]=nums[i],nums[s]
                BackTrack(s+1,e)
                nums[s],nums[i]=nums[i],nums[s]
        
        self.perms=[]
        BackTrack(0,len(nums))
        return self.perms
