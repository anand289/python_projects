def swap(input_list,a,b):
    temp = input_list[a]
    input_list[a] = input_list[b]
    input_list[b] = temp

def permutation_looper(numpad_list,start,end):
    if start == end:
        permutation_output.append(numpad_list.copy()) 
    else:
        for i in range(start,len(numpad_list)):
            swap(numpad_list,start,i)
            permutation_looper(numpad_list,start+1,end)
            swap(numpad_list,i,start)
    
            

numpad_list = [1,2,3]         
n = len(numpad_list)
permutation_output = []
permutation_looper(numpad_list,0,n-1)
print(permutation_output)

