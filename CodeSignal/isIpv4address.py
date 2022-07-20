def solution(a):
    def leadingZero(s):
        print(s)
        if s[0] =="0":
            if(int(s) >0):
                return False
            elif len(s)>1:
                return False
        return True
    l=-1
    c=0
    for r in range(len(a)):
        if a[r]==".":
            if a[l+1:r].isnumeric() and int(a[l+1:r]) >=0 and int(a[l+1:r]) <=255 and leadingZero(a[l+1:r]):
                c+=1
                l=r
            else:
                return False
    if a[l+1:].isnumeric() and int(a[l+1:]) >=0 and int(a[l+1:]) <=255 and leadingZero(a[l+1:]):
        c+=1
    else:
        return False
    if c==4:
        return True
    else:
        return False