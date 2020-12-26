
def sum(arr):
  sum = 0
  for elem in arr:
    sum += elem
  return sum


arrs = [[2,3,4], [3,5,7], [1,5,8]]
print(max(map(sum, arrs)))