class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        arr=preorder.split(",")
        l =len(arr)
        #print(l)
        if  l%2 ==0 or l<1:
            return False
        spots =1
        
        for i in range(l):
            if spots<=i:
                break
            if arr[i] != "#":
                spots+=2
        #print(spots)
        if spots !=l:
            return False
        return True
                
    
        
