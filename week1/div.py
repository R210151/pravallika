num1=float(input("enter the dividend: "))
num2=float(input("enter the divisor: "))
if num2 !=0:
	result=num1/num2
	print(f"{num1} divided by {num2} is {result}")
else:
	print("error: division by zero is not allowed")
