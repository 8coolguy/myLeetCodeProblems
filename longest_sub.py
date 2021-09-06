#learning the sliding windows technique
#longestsubstr

class Solution:
    #where do I go back dvdf
    #d
    # d v
    # d
    # d f
    def lengthOfLongestSubstring(self, s: str) -> int:
    #    def u_add(x,my_set):
    #        l =len(my_set)
    #        my_set.add(x)
    #        if len(my_set)==l:
    #            return False 
    #        return True
        my_set=set()
        maxLenStr =0
        #for c in s:
        #   if not u_add(c,my_set):
        #       l=len(my_set)
        #       if  l>maxLenStr:
        #           maxLenStr=l
        #       my_set=set()
        #       my_set.add(c)
        #   print(my_set)
        #l=len(my_set) 
        #if l > maxLenStr:
        #    return l
        #return maxLenStr
        i=0
        
        for c in range(len(s)+1):
            substr=s[i:c]
            #print(substr)
            #print(my_set)
            l=len(substr)
            if l>maxLenStr:
                maxLenStr =l
            if c !=len(s):
                while True:
                    if not my_set.__contains__(s[c]):
                        my_set.add(s[c])
                        break
                    else:
                        my_set.remove(s[i])
                        i+=1
        return maxLenStr
                
