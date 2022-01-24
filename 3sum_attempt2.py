#followed some youtube tutorial and i understand how nit works now it uses better logic for duplitcate detection and faster 2 sum search
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l=len(nums)
        my_arr =[]
        for i in range(l-1):
            if(i==0 or (i>0 and nums[i]!=nums[i-1])):
                lo =i+1
                h=l-1
                s=-1*nums[i]
                
                while(h>lo):
                    if(nums[lo]+nums[h]==s):
                        arr=[]
                        arr.append(nums[i])
                        arr.append(nums[lo])
                        arr.append(nums[h])
                        print(arr)
                        my_arr.append(arr)
                        while(h > lo and nums[lo] ==nums[lo+1]):
                                lo+=1
                        while (h >lo and nums[h]==nums[h-1]):
                                h-=1
                        lo+=1
                        h-=1
                    elif(nums[lo] +nums[h] > s):
                        h-=1
                    else:
                        lo+=1
        return my_arr
            #we then have to make sure the rest of the array is fine.
