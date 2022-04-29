class Solution:
    #lmao thats alot of if statements i could turn it into a if statement pretty easilt if I wanted
    def numberToWords(self, num: int) -> str:
        nums= ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        big=["Hundred","Thousand","Million","Billion"]
        def in100(y, place=None):
            ret=[]
            if y >99:
                ret.append(nums[int(y//100)])
                ret.append(big[0])
                y=y-(y//100*100)
                print(int(y))
            if y>19:
                
                ret.append(tens[int(y//10)])
                y=y-(y//10*10)
            if y!=0:
                ret.append(nums[y])
            
            if place:
                ret.append(place)
            return " ".join(ret)
            
        if num==0:
            return nums[0]
        res=[]
        if num >999999999:
            res.append(in100(int(num//(999999999+1)),big[-1]))
            num=num-(num//(999999999+1)*(999999999+1))
        if num >999999:
            res.append(in100(int(num//(999999+1)),big[-2]))
            num=num-(num//(999999+1)*(999999+1))
        if num >999:
            res.append(in100(int(num//(999+1)),big[-3]))
            num=num-(num//(999+1)*(999+1))
        if num >0:
            res.append(in100(int(num)))
        return " ".join(res)
        
        
        
        
        
    
            
                
        
        
            
            
        

