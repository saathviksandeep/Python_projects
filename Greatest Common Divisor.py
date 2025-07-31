num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))

while num2:
    num1, num2=num2, num1%num2
    print("The Greatest Common Divisor is",num1)