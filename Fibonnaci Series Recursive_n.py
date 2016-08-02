#Fibonnaci Series Recursive Solution
#Date Created:01-Aug-2016
#Sandeep Walia
def FibbonaciRecurive(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return FibbonaciRecurive(n-1)+FibbonaciRecurive(n-2)
		