class Solution:
    def isValid(self, s: str) -> bool:
        my_stack=[]
        my_dict ={'(':')','{':'}','[':']'}
        #iterate through sting
        for i in s:
            if(len(my_stack)==0):
                if(i not in my_dict):
                    return False
                my_stack.append(my_dict[i])
            else:
                if(my_stack[-1]==i):
                    my_stack.pop()
                else:
                    if(i not in my_dict):
                        return False
                    my_stack.append(my_dict[i])
                
        #final case
        if(len(my_stack)==0):
            return True
        return False
