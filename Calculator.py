# def add(x, y):
#     return x + y
#
#
# def subtract(x, y):
#     return x - y
#
#
def multiply(x, y):
    return x * y


#Divide - has error
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
if choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")
