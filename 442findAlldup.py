class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        #uses nums itseld as the storage for hash map
        res=[]
        for i in nums:
            if nums[abs(i)-1] <0:
                res.append(abs(i))
            else:
                nums[abs(i)-1]*=-1
        return res
        