#les get this codeSig streak again
def solution(a, b):
    c=0
    sa=[]
    sb=[]
    
    for i in range(len(a)):
        if a[i] != b[i]: 
            if c<2:
                sa.append(a[i])
                sb.insert(0,b[i])
            else:
                return False
    if sa==sb:
        return True
    else:
        return False
        
            
