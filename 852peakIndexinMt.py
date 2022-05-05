#bruh I can't beleive I can't even do these easy problems
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        hi =len(arr)-1
        lo=0
        m=0
        while hi>=lo:
            m=(hi+lo)//2
            #this line checks to see if the left ele is less and right is also less which means that its is the peak
            if arr[m - 1] < arr[m] > arr[m+1]:
                return m
            #checks to see of the right point is greater so we climb mountains
            elif arr[m] < arr[m + 1]:
                lo = m + 1
            #goes up the mountains the other way
            else:
                hi = m-1
            
