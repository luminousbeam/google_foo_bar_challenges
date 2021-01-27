def solution(xs):
  product = 1
  count = 0
  new_arr = []
  for i in range(len(xs)):
    if xs[i] < 0:
      count += 1
      xs[i] = abs(xs[i])
    if xs[i] == 0 or xs[i] == 1:
      continue
    else:
      new_arr.append(xs[i])

  for j in range(len(new_arr)):
    if count == 0 or count % 2 == 0:
      continue
    else:
      new_arr[0] = 1

  for k in range(len(new_arr)):
    product = product * new_arr[k]
  
  return product

# Input:
print(solution([2, -3, 1, 0, -5]))
# Output: 30

# Input:
print(solution([2, 0, 2, 2, 0]))
# Output: 8

# Input:
print(solution([-2, -3, 4, -5]))
# Output: 60
