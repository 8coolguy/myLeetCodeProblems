#interesting problem not sure if i could think of this but very cool soluiton
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        my_dict ={}
        stack=[]
        
        for i in s:
            if my_dict.__contains__(i):
                my_dict[i]+=1
            else:
                my_dict[i]=1
        #print(my_dict)        
        for i in s:
            print(my_dict)
            print(stack)
            if not i in stack:
                while(len(stack)!=0and stack[-1] >i and my_dict[stack[-1]] >0):
                    stack.pop()
                stack.append(i)
            my_dict[i]-=1
            
        res=''
        for i in stack:
            res+=i
            
        return res
                