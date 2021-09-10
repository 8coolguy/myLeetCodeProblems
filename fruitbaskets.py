#this problem is from the  grokkers course

def fruits_into_baskets(fruits):
  # ABCBBC
  #looking for max amount of fruits in each basket we can hold 
  #A max =1
  #AB,max 2
  #BC since there are 3 fruits we have to drop one and since a is earliest one we drop it max =2
  #BCB max =3
  #BCBB max =4
  #BCBBC since there was never a new one introduced the max is 5 
  max_fruits=0
  #use a set again to store the 2 fruits
  baskets =dict()
  total=0
  #only increment fruits when there is more than 2 fruits in the set 
  i =0
  for f in range(len(fruits)):
    if baskets.__contains__(fruits[f]):
      baskets.update({fruits[f]:baskets[fruits[f]]+1})
      total+=1
    else:
      baskets[fruits[f]]=1
      total+=1
      if len(baskets)>2:
        #remove fruit i
        total-=baskets.pop(fruits[i])
        i+=1
    if total>max_fruits:
      max_fruits =total
  return max_fruits

