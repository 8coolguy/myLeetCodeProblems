#got the wrong solution but found some resources that have this
#https://www.youtube.com/watch?v=6EfBJX9uLDI
#i need to learn the concept of dynamic programming
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        score=0
        
        
        while boxes != []:
            consecutive =[]
            c=0

            for i in range(len(boxes)):
                if i!=0:
                    if boxes[i] == boxes[i-1]:
                        consecutive[c-1].append(i)
                        continue
                temp =[]
                temp.append(i)
                consecutive.append(temp)
                c+=1

            maxConsecutive=maxIndex=0
            for i in range(len(consecutive)):
                temp=len(consecutive[i])
                if maxConsecutive<temp:
                    maxConsecutive=temp
                    maxIndex=i
            score+=maxConsecutive*maxConsecutive
            for i in consecutive[maxIndex]:
                boxes.pop(i)
        return score

                    
            
        
