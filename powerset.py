#not working dont no why
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def compareArr(arr1,arr2):
            print(arr1)
            print(arr2)
            if len(arr1) != len(arr2):
                return False
            for i in range(len(arr1)):
                if arr1[i] !=arr2[i]:
                    return False
            return True
        
        
        def checkRepeat(temp,ans):
            for i in range(len(ans)):
                if compareArr(ans[i],temp):
                    return False
                return True
            
            
            
        ans =[[]]
        c=1
        for i in range(len(nums)):
            temp =[]
            temp.append(nums[i])
            if (checkRepeat(temp,ans.copy())):
                ans.append(temp.copy())
                
            for j in range(i+1,len(nums)):
                temp.append(nums[j])
                if(checkRepeat(temp,ans.copy())):
                    ans.append(temp.copy())
        return ans