#very easy problem damn really got to work my way up to a 5 hour interview holy shitbruh
class Solution:
    def numberOfSteps(self, num: int) -> int:
        c=0
        while num !=0:
            c+=1
            print(num)
            if num%2==0:
                num=num//2
            else: num-=1
        return c