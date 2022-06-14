def solution(s1, s2):
    a={}
    b={}
    
    for i in s1:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
    for i in s2:
        if i in b:
            b[i]+=1
        else:
            b[i]=1
    tot=0
    for i in list(a.keys()):
        if i in b:
            tot+=min(b[i],a[i])
    return tot

