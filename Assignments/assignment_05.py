# Problem 1: Is it a valid matrix?
def is_valid_matrix(matrix):
  new_list = []
  is_valid = True
  
  for i in range(len(matrix)):
    new_list.append(len(matrix[i]))
  
  for num in range(len(new_list)):
    previous_number = new_list[0]
    if num == 0:
      continue

    if previous_number != new_list[num]:
      is_valid = False
      return is_valid
    
  return is_valid


print(is_valid_matrix([[1,2,3],[4,5,6],[7,8,9]]))
print(is_valid_matrix([[1,2,3],[4,5],[7,8,9]]))


# Problem 2: Matrix multiplication

def matrix_multiply(m, n): # m is the first matrix and n is the second matrix
  # Check if matrices are valid
  # Check if num of collumns of matrix 1 is equal to the number of rows of matrix 2
  if ( is_valid_matrix(m) and is_valid_matrix(n) ) and (len(m[0]) == len(n)):
      result_matrix = []
      for r in range(len(m)):
        result_matrix.append([])
        for row in range(len(m)):
          multiplication = 0
          for col in range(len(m[0])):
            # 0-012 1-123
            multiplication += m[r][col] * n[col][row]
            
          result_matrix[r].append(multiplication)

      return result_matrix

  else:
    return None # Return none if matrices are invalid

 

matrix1 = [[1,2,3], [4,5,6]]
matrix2 = [[1,2], [3,4], [5,6]]

print(matrix_multiply(matrix1, matrix2))
print(matrix_multiply(matrix2, [[]]))
print(matrix_multiply(matrix2, matrix2))