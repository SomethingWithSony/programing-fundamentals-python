# Problem 1: Is number in list?

def is_in_list(n, lst):
  in_list = False

  for i in lst:
    if n == i:
      in_list = True
      break

  return in_list

"""
print(is_in_list(5, [1,2,3,4]))
print(is_in_list(5, [1,5,6]))
"""
# Problem 2: Intersection of lists

def intersection(lst1, lst2):
  new_list = []
  
  for num1 in lst1:
    for num2 in lst2:
      if (num1 == num2) and (num1 not in new_list):
        new_list.append(num1) 
        
  return new_list
  

print(intersection([1,2,3], [2,4,6]))
print(intersection([1,2,3], [4,5,6]))
print(intersection([2,3,2,4], [2,2,4]))


