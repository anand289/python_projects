#Commons in two arrays.
from performance import performance
from random import randint

@performance
def common_elements_naive(arr1,arr2):
  commons = []
  n = max(len(arr1),len(arr2))
  for i in range(0,n):
    if i in arr1 and i in arr2:
      commons.append(i)
  return commons

arr1 = []
arr2 = []

for i in range(0,1000):
  arr1.append(randint(0,1000))
  arr2.append(randint(0,1000))


print(common_elements_naive(arr1,arr2))