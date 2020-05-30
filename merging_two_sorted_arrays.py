#Merging two sorted arrays
from performance import performance

@performance
def bubble_sort(arr1,arr2):
	merge = arr1 + arr2
	for i in range(0,len(merge)):
		for j in range(i+1,len(merge)):
			if merge[i] > merge[j]:
				temp = merge[i]
				merge[i] = merge[j]
				merge[j] = temp
	print(merge)
	return

@performance
def mergeSortedArrays2(arr1,arr2):
	merge = arr1 + arr2
	print(sorted(merge))
	return



bubble_sort([9,3,5,7,9,4,5,6,5,4,2,2345,456,3456,2345,145134,]
	       ,[2,4,24356,6,7,12,234,456,456,0,145,9,9,2345,245,8])




