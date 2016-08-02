#Sum of a GP
#Date Created:01-Aug-2016
#Sandeep Walia
def GPSum(n,r):
	prod,sum=1,0
	i=n 
	while i>=0:
		for j in range(i+1):
			prod*=n 
		sum+=prod
		i-=1
		prod=1
	return sum
print GPSum(2,3)


			