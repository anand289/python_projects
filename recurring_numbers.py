from performance import performance
from random import randint


#O(n^2)
@performance
def recurring_number_naive(arr):
    for i in range(0, len(arr)):
        for j in range(i-1,-1,-1):
            if arr[i] == arr[j]:
                return print(f'{arr[i]} is the recurring number.')

@performance
def recurring_number(arr):
    new_arr = [] 
    for i in arr:
        if i in new_arr:
            return print(f'{i} is the recurring number.')
        new_arr.append(i)

@performance
def recurring_number_hash(arr):
    map = {}
    for i in range(0, len(arr)):
        if arr[i] in map.keys():
            return print(f'{arr[i]} is the recurring number.')
        else:
            map[arr[i]] = i
    return 0


arr = []
#difference in time starts to appear only for crazy huge input.
for i in range(0,100):
  arr[i] = arr.append(randint(0,10))#to get each input between 0-10.


print(recurring_number_naive(arr))
print(recurring_number(arr))
print(recurring_number_hash(arr))
