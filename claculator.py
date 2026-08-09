# Simple Calculator using if, elif, else

print("Simple Calculator")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter operator (+, -, *, /): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "+":
    print("Result =", num1 + num2)

elif choice == "-":
    print("Result =", num1 - num2)

elif choice == "*":
    print("Result =", num1 * num2)

elif choice == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid operator! Please enter +, -, *, or /.")
    