# Problem 1: Is List Increasing order?

def is_increasing(lst):
  # Base Case
  if len(lst) < 3:
    if lst[0] < lst[1]:
      return True
    else:
      return False

  # Recursion Case
  else:
    if lst[0] > lst[1]:
      return is_increasing([lst[0], lst[1]])
    else:
      return is_increasing(lst[1:])


print(is_increasing([1,2,3,4]))
print(is_increasing([1,3,2,4]))


# Problem 2: Numbers greater than n

def filter_gt_n(lst, n): 
  # Base Case
  if not lst:
    return lst
  # Recursion Case
  else:
    # Check if list
    if type(lst[0]) == list:
      # Check if list is empty
      if not lst[0]:
        return lst[1]
      else:
        
        if lst[0][0] > n :
          filter_gt_n([lst[0][1:],lst[1]], n)
        else:
          lst[0].remove(lst[0][0])
          filter_gt_n(lst, n)

        return lst[1]

      
    else:
      if lst[0] > n :
        filter_gt_n([lst[1:],lst], n)
      else:
        lst.remove(lst[0])
        filter_gt_n([lst,lst], n)

      return lst


print(filter_gt_n([1,2,3,4], 2))
print(filter_gt_n([2,2,3,3], 4))


# Problem 3 (Challenge): Find the intersection of two lists
def intersection(lst1, lst2):
  # Base Case
  if not lst1:
    
    return helper_function3(lst2[0],helper_function2([], lst2), [])
  # Recursion Case
  else:
    if lst1[0] == helper_function(lst1[0],lst2):
      lst2.append(lst1[0])
    else:
      pass
      
    return intersection(lst1[1:], lst2)
    

# Iterate
def helper_function(n, lst2):
  # Base Case
  if not lst2:
    return "No Match"
  else:
    if n == lst2[0]:
      return n 
    else: 
      return helper_function(n,lst2[1:])
  # Recursion Case


# Returns list with only duplicated elements
def helper_function2(empty_list,lst2 ):
  # Base Case
  if not lst2:
      return empty_list
  else:
  # Recursion Case
    if lst2.count(lst2[0]) == 1:
      lst2.pop(0)
    else:
      empty_list.append(lst2[0])
  
    
  return helper_function2(empty_list,lst2[1:])


# Removes duplicated occurences 
def helper_function3(n,lst1,lst2):
  # Base Case
  if not lst1:
    return lst2
  # Recursion Case
  else:
    
    n = lst1[0]
    
    if n == lst1[0]:
     
      if n in lst2:
        return helper_function3(n,lst1[1:],lst2)
      else:
        lst2.append(n)
        return helper_function3(n,lst1[1:],lst2)
    
      
      
    return helper_function3(n,lst1[1:],lst2)
    
print(intersection([1,2,3], [2,4,6]))
print(intersection([1,2,3], [4,5,6]))
print(intersection([2,3,2,4], [2,2,4]))
