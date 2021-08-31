class Solution:
    def findMin(self, nums: List[int]) -> int:
        l =len(nums)
        if l==0:
            return -1
        if l==1:
            return nums[-1]
        hi=l-1
        lo=0
        while(hi>lo):
            mid =int((hi+lo)/2)
            #print(mid)
            if mid >0 and nums[mid]<nums[mid-1]:
                return nums[mid]
            elif nums[lo] <= nums[mid] and nums[mid] >nums[hi]:
                lo =mid+1
            else:
                hi=mid -1
            #print(f"{hi}--------{lo}")
        return nums[lo]

