# Restriction use only while loops
# Problem 1: FizzBuzz
def fizzbuzz(n):
  i = 0

  while i <= n:
    multiple_of_3 = i % 3 == 0
    multiple_of_5 = i % 5 == 0

    if multiple_of_3 and multiple_of_5:
      print("fizzbuzz")
    elif multiple_of_3:
      print("fizz")
    elif multiple_of_5:
      print("buzz")

    else:
      print(i)

    i += 1

  return


fizzbuzz(15)

# Problem 2: Multiply without *
def multiply(a, b):
  i = 1
  initial_a = a
  initial_b = b

  if b < 0:
    b = -b

  while i < b:
    i += 1
    a += initial_a

  if (a < 0) and (initial_b < 0):
    a = -a

  return a



print(multiply(3, 5))
print(multiply(-4, 5))
print(multiply(-4, -2))


# Problem 3: Output the first n prime numbers
def prime_numbers(n):
  i = 0
  while i < n:
    divisible_by_2 = i % 2 == 0
    divisible_by_3 = i % 3 == 0
    
    if i > 1:
      if ((i == 2) and divisible_by_2) or ((i == 3) and divisible_by_3):
        print(i)
      elif (divisible_by_3 == False) and (divisible_by_2 == False):
        print(i)
        
    i += 1

  return
  

prime_numbers(100)
