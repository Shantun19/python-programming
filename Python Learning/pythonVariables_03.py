"""
A python variable is used to store any type of data.
in pyhton you don't need to declare the type of the variable.In python variable are dynamically typed.
"""
age = 12
name = "Peter"
print(f'My name is {name} and i m {age} year old') # My name is Peter and i m 12 year old

"""
Rules to declare a varaible
    - Names can contain letters, digits and underscores (_).
    - The first character cannot be a digit.
    - Names are case-sensitive, so myVar and myvar are treated differently.
    - Keywords such as if, else and for cannot be used as variable names.

Below listed variable names are valid:
    age = 21
    _colour = "lilac"
    total_score = 90
Below listed variables names are invalid:
    1name = "Error"  # Starts with a digit
    class = 10       # class is a reserved keyword
    user-name = "Doe"  # Contains a hyphen
"""

"""
Assigning Values to Variables
"""

"""
1. Basic Assignment: Variables are assigned values using the = operator.
"""
num = 10
username = "peter10"

"""
2. Dynamic Typing: Python is dynamically typed, so the same variable can store different data types during execution.
"""
x = 20
x = "change the type of the variable at the runtime"

"""
3. Assigning Same Value: Same value can be assigned to multiple variables in a single line.
"""
a = b = c = 100
print(a , b , c)

"""
4. Assigning Different Values: Multiple variables can also be assigned different values in a single line.
"""
x , y , z = 1 , 2 , 3
print(x , y , z)

"""
Concept of Object Reference
Let us assign a variable x to value 5. x = 5 - When x = 5 is executed, Python creates an object to represent the value 5 and makes x reference this object.
    x -------------> 5
Now, let's assign another variable y to the variable x. y = x
    x -------------> 5 <------------- y
Now, if we write x = 'Geeks' - Python creates a new object for the value "Geeks" and makes x reference this new object.
    y -------------> 5
    x -------------> Geek
The variable y remains unchanged, still referencing the original object 5. Now, If we assign a new value to y: y = "Computer"
    y -------------> computer
    x -------------> Geek
      -------------> 5 - is collected by the garbage collector
"""

"""
Deleting a Variable
    - del keyword is used to delete a variable from memory. After deletion, the variable can no longer be accessed.
    - What does Garbage Collection do?
        - Garbage Collection automatically identifies objects that are no longer needed and reclaims their memory.
    - What does del do?
        - The del keyword removes a reference (such as a variable name) from Python's namespace.
        - You can no longer access the variable using the name.
        - Important: del does not directly delete the object from memory. It removes a reference.
        - Manually executed by the programmer.
"""
x = 10
del x
print(x) # error - Traceback (most recent call last): File "<main.py>", line 3, in <module> NameError: name 'x' is not defined
