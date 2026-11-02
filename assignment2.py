#task 1
def calculator():
    print(" BASIC CALCULATOR")
    num1 = int(input("enter a number"))
    num2 = int(input("enter another number"))
    op = input("enter operation(+,-,*,/,//,%):")
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "//":
        print(num1 // num2)
    elif op == "%":
        print(num1 % num2)
    else:
        print("invalid operator")
calculator()

#task 2
n=int(input("enter number of rows"))
if n<=0:
    print("enter number greater than 0")
else:
    for i in range(1,n+1):
       for j in range(i,0,-1):
        print(j,end=" ")
       print()



