#Largest Element in an Array
#Date Created:01-Aug-2016
#Sandeep Walia
def LargestElement(arr,n):
	max=arr[0]
	for i in range(2,n):
		if(arr[i]>max):
			max=arr[i]
	return max
newarr=[]
newarr.extend([3,5,99,66,75,95,25]);
print LargestElement(newarr,7);