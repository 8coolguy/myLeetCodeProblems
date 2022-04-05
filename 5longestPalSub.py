#wow after almost a year I got the 5th problem done im asmart 2 inters method 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s):
            l=len(s)

            if l%2==0:
                l=l//2
                s1=s[:l]
                s2=s[l:]
            else:
                l=l//2
                s1=s[:l+1]
                s2=s[l:]
            s2=s2[::-1]
            if s2==s1:
                return True
            else:
                return False
        res=""
        #for i in range(len(s)+1,0,-1):
        #   for j in range(len(s)-i+1):
        #        res=s[j:j+i]
        #        if isPalindrome(res):
        #            return res

        n =len(s)
        for i in range(0,n):
            right =i
            while right < n and s[i] ==s[right]:
                right+=1

            left =i-1
            while left >=0 and right <n and s[left]==s[right]:
                left-=1
                right+=1
            print(s[left+1:right])
            if len(s[left+1:right]) >len(res):
                res=s[left+1:right]
        return res









