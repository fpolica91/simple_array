
# get the minimum array value

numbers = [1,4,6,7,9,77,0]

def get_min(arr):
#initialize min to infinity
  min_arr = float('inf')
  # iterate over array
  for elem in arr:
    if elem < min_arr:
       min_arr = elem
  return min_arr


def get_max(arr):
  max_number = float('-inf')
  for elem in arr:
    if elem > max_number:
      max_number = elem
  return max_number

def get_sum(arr):
  sum_arr = 0;
  for elem in arr:
    sum_arr += elem
  return sum_arr


  
print(get_min(numbers))
print(get_max(numbers))
print(get_sum(numbers))

