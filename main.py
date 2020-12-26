from map import *
from max_sum_array import *
# get the minimum array value

numbers = [1,4,6,7,9,77,0]
deep = [1,2,3, [1,2,3,4], [4,55,55]]

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


# copy elements from array
def simple_copy(arr):
  copy = []
  for elem in arr:
    copy.append(elem)
  return copy

# Deep copy of elements from array
def deep_copy(arr):
  if not isinstance(arr, list):
    return arr
  else:
   return [deep_copy(elem) for elem in arr]
  

# joining elements
def join_array(arr, separator):
  joined =""
  for i in range(len(arr)):
    joined += str(arr[i])
    if i < len(arr) -1:
      joined += separator
  return joined

#concatenate
def concatenate(arr1, arr2):
  conc = []
  for elem in arr1:
    conc.append(elem)
  for elem in arr2:
    conc.append(elem)
  return conc

def extend(arr1,arr2):
  for elem in arr2:
    arr1.append(elem)
  return arr1

def sum(n):
 print(n)
 if n == 0:
   return 0
 else:
   return sum(n - 1) + n

 



# print(get_min(numbers))
# print(get_max(numbers))
# print(get_sum(numbers))
# print(simple_copy(numbers))
# print(deep_copy(deep))
# print(join_array([1,2,3], "*"))
# print(concatenate([1,2,3], [3,5,6]))
# print(extend([1,2,3], [2,3,4]))
# print(sum(4))
