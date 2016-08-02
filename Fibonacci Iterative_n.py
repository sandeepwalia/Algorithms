#Fibonacci Iterative
#Date Created:01-Aug-2016
#Sandeep Walia

#http://stackoverflow.com/questions/493386/how-to-print-in-python-without-newline-or-space
from __future__ import print_function #to use advanced Print function(Source Provided Above)
def fibonacciIterative(n):
	a,b=0,1
	for i in range(n):
		print (a,end=" ")
		a,b=b,a+b
	return a
number=int(raw_input("Enter Number"))
fibonacciIterative(number)