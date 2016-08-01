#Recursive Factorial
#Date Created:01-Aug-2016
#Sandeep Walia
def factorial(n):
	if n==1:
		return 1
	else:
		res=n*factorial(n-1)
		return res
a=int(raw_input("Enter a number"))
print(factorial(a))
