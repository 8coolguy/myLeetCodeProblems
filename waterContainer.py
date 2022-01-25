#once again my solution did not work because of the time restraint
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if height == None:
            return 0
        n =len(height)
        # take the 2 highes highes take the sum and go through the rest
        new_height=list(height)
        height.sort()
        maximum=0
        my_dict={}
        for i in range(n):
            if my_dict.__contains__(new_height[i]):
                my_dict[new_height[i]].append(i)
            else:
                tmp=[]
                tmp.append(i)
                my_dict[new_height[i]]=tmp
        #print(my_dict)
        
        for i in range(n):
            for i2 in range(n):
                if i==i2:
                    continue
                for j in range(len(my_dict[height[i2]])):
                    for k in range(len(my_dict[height[i]])):
                        #print(min(height[i],height[i2])*abs(my_dict[height[i2]][j]-my_dict[height[i]][k]))
                        if(min(height[i],height[i2])*abs(my_dict[height[i2]][j]-my_dict[height[i]][k]) > maximum):
                            maximum =min(height[i],height[i2])*abs(my_dict[height[i2]][j]-my_dict[height[i]][k])
        return maximum
