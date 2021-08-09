#gave it a good effort but took too long but i was very clode and it worked on the base cases not the fi#ll submission

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        def checkIfChecked(nextCheck,check):
            i=nextCheck.split("-")
            for ele in check:
                j=ele.split("-")
                if i[0]==j[-1] and i[-1]==j[0]:
                    return False
            return True
            
        m=len(matrix)
        n=len(matrix[0])

        ans=[ [1 for i in range(n)] for _ in range(m)]
        for i in range(n):
            check=[]
            for arr in range(m):
                for  i in range(n):
                    for y in range(m):
                        for x in range(n):
                            temp="{}{}-{}{}".format(arr,i,x,y)
                            if arr ==y and x ==i:
                                continue
                            elif arr==y or x==i and checkIfChecked(temp,check):
                                check.append(temp)
                                if matrix[arr][i] > matrix[y][x] and ans[y][x]<=ans[arr][i]:
                                    ans[arr][i]+=1
                                elif matrix[arr][i] < matrix[y][x] and ans[y][x]<=ans[arr][i]:
                                    ans[y][x]+=1
                                elif matrix[arr][i] == matrix[y][x] and ans[y][x]!=ans[arr][i]: 
                                    ans[arr][i]=ans[y][x] =max(ans[y][x],ans[arr][i])
                                    
