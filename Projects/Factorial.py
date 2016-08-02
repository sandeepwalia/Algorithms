#Q. Write a non-recursive method to compute the factorial of n 
#02-Aug-2016
#Sandeep Walia	
def factorial(n):
	fact=1
	if n==0:
		return 1
	for i in range(2,n+1):
		fact*=i 
	return fact 
print factorial(100)

