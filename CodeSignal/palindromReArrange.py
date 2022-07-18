#ez work
def solution(inputString):
    my_dict={}
    for i in inputString:
        if i in my_dict:
            my_dict[i]+=1
        else:
            my_dict[i]=1
    print(my_dict)
    oneodd=False
    for i in my_dict.keys():
        if my_dict[i]%2==1 and oneodd:
            return False    
        elif my_dict[i]%2==1 and not oneodd:
            oneodd =True
    return True