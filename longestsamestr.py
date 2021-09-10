def length_of_longest_substring(str, k):
  #aabbccaa k=4
  #aabb   a2b2 k=4->a4b4
  #aabbc  a2b2c1 k=4 ->a5 b5
  #aabbcc a2b2c2 k=4->a6b6c6
  #aabbcca a3b2c2 k=4->a7
  #aabbccaa a4b2c2 k=4>a8
  #8
  #ggaabbccaa
  #myb look at the k+1 characters
  #ggaab g2a2b1 k=4 g5a5
  #ggaabb g2a2b2 k=4 g6a6b6
  #ggaabbc g2a2b2c1 k=4->0
  #when the total of the other elements are greater than K increment i
  #take largest element in the dictionary
  total=0
  i=0
  max_len=0
  #we dont care what we just need the value of the thing
  largest_char=0
  my_dict=dict()
  for c in range(len(str)):
    if my_dict.__contains__(str[c]):
      my_dict.update({str[c]:my_dict[str[c]]+1})
      val=my_dict[str[c]]
      print(val)
      if val>largest_char:
        largest_char =val
    else:
      my_dict[str[c]] =1
    
    if total-largest_char>k:
      if my_dict[str[i]] >1:
        my_dict.update({str[i]:my_dict[str[i]]-1})
      else:
        my_dict.pop(str[i])
      i+=1
      total-=1
    
    if max_len < total:
      max_len =total
    total+=1
    print(my_dict)
    print(str[i:c+1])
  print(max_len)
  return max_len




