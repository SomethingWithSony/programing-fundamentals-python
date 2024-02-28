# Problem 1: Generate list of numbers


def generate_list(start, end, step):
  new_list = []
  step = abs(step)
  initial_step = step

  if start < end:
    while start < end:
      if step == 0:
        step = initial_step

      if step == initial_step:
        new_list.append(start)

      step -= 1
      start += 1
  else:
    while end < start:
      if step == 0:
        step = initial_step

      if step == initial_step:
        new_list.append(start)

      step -= 1
      start -= 1

  return new_list


print(generate_list(0, 5, 1))
print(generate_list(0, 0, 1))
print(generate_list(5, 10, 2))
print(generate_list(10, 5, -2))


# Problem 2: Reverse the list

def reverse_list(lst):
  return lst[::-1]

print(reverse_list([1,2,3,4,5]))