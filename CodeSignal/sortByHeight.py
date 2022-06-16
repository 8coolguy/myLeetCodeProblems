#ok weird problem but antother code signal in the books
def solution(a):
    x=sorted(a)
    i=0
    while i != len(x):
        if x[i]==-1:
            x.pop(i)
        else:
            i+=1
    i=0
    for j in range(len(a)):
        if a[j] != -1:
            a[j]=x[i]
            i+=1
    return a
            
        