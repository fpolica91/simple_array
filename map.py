def mult(n):
  return n*2


def map(arr, func):
  new_arr = []
  for elem in arr:
    new_arr.append(func(elem))
  return new_arr

  print('hello world')



print(map([1,2,3], mult))