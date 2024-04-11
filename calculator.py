#Create a simple calc

#9/4/23

#set up functions
def add(x, y):
    return x + y
def minus(num1, num2):
    return num1 - num2
def divide(num1, num2):
    return num1 / num2
def multiply(num1, num2):
    return num1 * num2
def remainder(num1, num2):
    return num1 % num2


#enter variables
num1 = int( input( "Enter first number:"))
num2 = int( input( "Enter second number:"))

#let the user to choose an operand
sign = input( "Enter the Operand sign: " )

if sign == '+':
    print( add(num1, num2))
elif sign == '-':
    print( minus(num1, num2))
elif sign == '*': 
    print( multiply(num1, num2))
elif sign == '/': 
    print( divide(num1, num2))
elif sign == '%':
    print( remainder(num1, num2))
else:
    print("wewe ni mujinga!!!!!")







