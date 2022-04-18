class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #i think my solution but it runs out of time it was brute 
        #if s=="":
        #    return True
        
        #for i in range(len(s)+1):
        #    #print(s[:i])
        #    if wordDict.__contains__(s[:i]):
        #        if self.wordBreak(s[i:], wordDict):
        #            return True
        #return False
        #this is the sp solution which i get 
        #creates dp arr
        dp= [False]*len(s)
        #iterates through all the chars
        for i in range(len(s)):
            #for each word it checks if the sub string of len of the word == to word then it goes backs and checks if the rest of the s is good throught the dp array
            for w in wordDict:
                if w==s[i-len(w)+1:i+1] and (dp[i-len(w)] or i-len(w) == -1):
                    dp[i]=True
        #return the last one
        return dp[-1]
        
