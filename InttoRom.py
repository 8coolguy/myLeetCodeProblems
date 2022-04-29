class Solution:
    #had to look at a solution which was understandable but  ot that intuitveZZ
    def intToRoman(self, num: int) -> str:
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res=""
        for i,j in enumerate(values):
            res+= (num//j)*numerals[i]#max value that num can go is 3 get the num of times i need a char
            num%=j #gets the amount 
        return res
