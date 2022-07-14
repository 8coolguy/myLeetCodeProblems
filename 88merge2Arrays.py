class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return 
        p1=0
        p2=0
        c=0
        while p2 < n:
            if c < m and nums1[p1] < nums2[p2]:
                c+=1
            elif p2 < n:
                print("two")
                for i in range(len(nums1)-1,p1,-1):
                    tmp = nums1[i]
                    nums1[i] =nums1[i-1]
                    nums1[i-1]=tmp
                nums1[p1] = nums2[p2]
                p2+=1
            p1+=1
                    
                    
                
        