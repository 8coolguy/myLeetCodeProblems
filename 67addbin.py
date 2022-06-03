class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def bita(a,b,c):
            if c=="1":
                if a =="1" and b=="1":
                    return "1",c
                elif (a=="1")^(b=="1"):
                    return "0",c
                return "1","0"
            else:
                if a =="1" and b=="1":
                    return "0","1"
                elif (a=="1")^(b=="1"):
                    return "1","0"
                return "0","0"
            
            
        carry=["0"]
        res=""
        for i in range(max(len(a),len(b))):
            ba=""
            bb=""
            if len(a) <=i:
                ba="0"
            else:
                ba=a[-1-i]
            if len(b) <=i:
                bb="0"
            else:
                bb=b[-1-i]
            tmp,c=bita(ba,bb,carry[0])
            
            carry.insert(0,c)
            
            res=tmp+res
        if carry[0]=="1":
            res= "1"+res
        return res
                
                
            
                
        