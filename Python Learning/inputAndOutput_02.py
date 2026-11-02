# The print() function is used for output in various formats and the input() function enables interaction with users.
"""
Taking Input using input() - Python's input() function is used to take user input. By default, it returns the user input in form of a string. 
"""
var = input("Enter any value")
print(var)

"""
input() Function Working
    - You can optionally provide a prompt message (e.g., "Enter your age:").
    - Whether you type letters, numbers, or symbols, Python always stores it as a string by default.
    - If you need another data type (like integer or float), you must convert it manually using typecasting.

Example: This program checks the data type of user input to confirm that both number and name are stored as strings.
"""
num = input("Enter number:")
print(num)
name1 = input("Enter name: ")
print(name1)

# Printing type of input value
print("Type of number:", type(num)) # <class 'str'>
print("Type of name:", type(name1)) # <class 'str'>

"""
Converting Input into Numbers - Often, you need numerical input (like age, marks, or salary). Since input() returns a string, you must convert it using int() or float().
"""
num = int(input("Enter a number: "))
print(num, "is of type", type(num))
floatNum = float(input("Enter a decimal number: "))
print(floatNum, "is of type", type(floatNum))

"""
Taking Multiple Inputs-Sometimes, a program needs to accept more than one value at once. In Python, this can be done by entering values separated by spaces and then splitting them into separate variables.
"""
x, y = input("Enter two numbers separated by space: ").split()
print("First number:", x)
print("Second number:", y)