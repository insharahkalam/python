num1 = int(input("Enter Your 1st Number: "))
operator = input("Enter Your operator: ")
num2 = int(input("Enter Your 2nd Number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "**":
    print(num1**num2)
elif operator == "//":
    print(num1 // num2)
else:
    print("Invalid input!")
