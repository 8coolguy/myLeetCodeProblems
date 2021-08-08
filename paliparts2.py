#did not understande this very well 
#found a page on how to solve this ill take a look later 
# https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/
#
#
#
#
#had to use recursion lieke alot of problems need me to do
#the code I wrote down so far
class Solution:
    def minCut(self, s: str) -> int:
        def isPali(arr):
            for i in range(len(arr)):
                if arr[i]!=arr[-1-i]:
                    return False
            return True

        #most extreme case is a cut every single letter
        #it would look like this
        #cuts=0
        #for i in range(len(s)):
        #   print(s[i:i+1])
        #   cuts+=1
        countingCuts=True
        c=1
        while countingCuts:
            splited =True
            for i in range(c):
                newS =s[i:len(s)-i]
                if  not isPali(newS):
                    splited =False
                    break
            if splited:
                return c-1
            c+=1

