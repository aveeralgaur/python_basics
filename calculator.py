#Simple Calculator
user_input=int(input("1 For Addition 2 For Substraction 3 For Multiplication 4 For Division: "))
if user_input==1:
	input1=input("Value1: ")
	input2=input("Value2: ")
	print(input1+input2)
elif user_input==2:
	input1=input("Value1: ")
	input2=input("Value2: ")
	print(input1-input2)
elif user_input==3:
	input1=input("Value1: ")
	input2=input("Value2: ")
elif user_input==4:
	input1=input("Value1: ")
	input2=input("Value2: ")
else:
	print("Wrong input")