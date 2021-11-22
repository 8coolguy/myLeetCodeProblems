class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #wait wut
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)
        
