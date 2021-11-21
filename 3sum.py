#my solution has a run time of On^3 and does not pass the leet code tests cause its too long
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def checkIf(arr,res):
            for i in res:
                my_set=set(i)
                if(arr[0]==0 and arr[1]==0 and arr[2]==0):
                    if(arr[0]==i[0] and i[1]==arr[1] and i[2]==arr[2]):
                        return False
                    else:
                        continue
                if(arr[0] in my_set and arr[1] in my_set and arr[2] in my_set):
                    return False
            return True
        #you need to have a pointer to each of the three
        my_arr=[]
        if (len(nums)<=2):
            return my_arr
        ptr1=0
        while(ptr1 <len(nums)):
            ptr2=ptr1+1


            while(ptr2<len(nums)):
                ptr3=ptr2+1
                total=(nums[ptr1]+nums[ptr2])*-1

                while(ptr3<len(nums)):
                    triple=[]
                    if(nums[ptr3]==total):
                        triple.append(nums[ptr1])
                        triple.append(nums[ptr2])
                        triple.append(nums[ptr3])
                        if(checkIf(triple,my_arr)):
                            my_arr.append(triple)
                    ptr3+=1
                ptr2+=1
            ptr1+=1
        return my_arr

