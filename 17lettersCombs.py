#not my solution but i understand the dfs solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[]
        s=[]
        def dfs(digits):
            if not digits:
                res.append("".join(s))
                return
            for i in d[digits[0]]:
                s.append(i)
                dfs(digits[1:])
                s.pop()
        if digits:
            dfs(digits)
        return res
    
