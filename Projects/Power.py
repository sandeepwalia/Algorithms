#Write a non-recursive method to compute x^n
#02-Aug-2016
#Sandeep Walia
def pow(x,n):
	if n==0:
		return 1
	product,i=1,0
	while i<n:
		product*=x
		i+=1
	return product
print pow(55,2)
print pow(2,3)