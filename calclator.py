def addition():
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    result = first + second
    print(result)


def subtraction():
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    result = first - second
    print(result)


def multiplication():
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    result = first * second
    print(result)


def division():
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    result = first / second
    print(result)


def modulo():
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    result = first % second
    print(result)


print("1=addition, 2=subtraction, 3=multiplication, 4=division, 5=modulo")
option = int(input("Enter your option:"))

if option == 1:
    addition()
elif option == 2:
    subtraction()
elif option == 3:
    multiplication()
elif option == 4:
    division()
else:
    modulo()




