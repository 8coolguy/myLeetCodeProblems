#ok dp looking nice bois
class Solution:
    def countAndSay(self, n: int) -> str:
        print(f'**{n}**')
        dp=["1"]
        for i in range(2,n+1):
            res=""
            tmp=dp[-1]
            c=0
            char=""
            for i in tmp:
                print(i)
                if i != char:
                    if c!=0:
                        res = res + str(c)+char
                    char=i
                    c=1
                else:
                    c+=1
            res = res + str(c)+char
            dp.append(res)
        return dp[-1]
                    
            
        