#code signal questions are pretty simple so far i might startdoing some hackerrank
def solution(n):
    k=int(n)
    c=0
    while k!=0:
        k=k//10
        c+=1
    h=c//2
    tot_h1=0
    for _ in range(h):
        tot_h1+=n%10
        n=n//10
    tot_h2=0
    for _ in range(h):
        tot_h2+=n%10
        n=n//10

    return tot_h1 ==tot_h2