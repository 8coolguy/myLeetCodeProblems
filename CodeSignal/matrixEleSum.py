def solution(matrix):
    #take transpose and count unitl 0
    m=len(matrix)
    k=len(matrix[0])
    trans=[[matrix[j][i] for j in range(m)] for i in range(k)]
    tot=0
    for j in trans:
        for i in j:
            if i!=0:
                tot+=i
            else:
                break
    return tot
        
    



