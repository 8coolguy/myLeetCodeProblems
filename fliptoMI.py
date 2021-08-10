# didnt get this one but the answer was super easy but i didn really get it 
# resource https://www.tutorialspoint.com/flip-string-to-monotone-increasing-in-cplusplus
# my solution passed 50/90 and had a time complexity of o(n3+2On)not sure of space complecity

class Solution:
    #define monotone increasing
    #   the number of 0s is less than or equal to the number of 1s that follows
        flip0, flip1 = 0, 0
        for c in S:
            flip0 += int(c == '1')
            flip1 = min(flip0, flip1 + int(c == '0'))
        return flip1
    #need to make a min num of changes to make it monotone increasing as shown below\
        def isMonotoneIncreasing(bs):
            numOf0s=0
            numOf1s =0
            for i in range(len(bs)):
                if bs[i] =="0":
                    numOf0s+=1
                elif bs[i]== "1":
                    if i !=len(bs)-1 and bs[i+1]=="0":
                        return False
                    numOf1s+=1
            
            return True
        def count(bs):
            ls=0
            os=0
            for i in bs:
                if i=="0":
                    os+=1
                else:
                    ls+=1
            return os,ls
                    
        os,ls=count(s)
        temp=list(s)
        cuts=0
        while not isMonotoneIncreasing(temp):
            temp=list(s)
            cuts+=1
            for i in range(cuts):
                for j in range(len(temp)):
                    if os-cuts>ls:
                        if j!=len(temp)-1 and int(temp[j]) >int(temp[j+1]):
                            temp[j]=str(temp[j+1])
                            break

                    elif ls-cuts>os:
                        if j!=len(temp)-1 and int(temp[j]) >int(temp[j+1]):
                            temp[j+1]=str(temp[j])
                            break
                       
                        
            
            print(temp)
            

        return cuts
        
