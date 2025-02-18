# This is how to comment on one line.

"""
This is how to comment
on more than one line.
"""

# Create Variable:
x = 5
y = "John"
print(x, y) # Expected Output = 5 John

x = 4 # Type Int
x = "Sally" # Type String
print(x) # Expected Output = Sally

# Casting
x = str(3)
y = int(3)
z = float(3)

# Get Type of Variable
x = 5
y = "John"
print(type(x), type(y), type(z)) # Expected Output = <class 'int'>, <class 'str'>, <class 'float'>
print(type(x)) # Expected Output = <class 'int'>

# Single or Double Quotes Either Way
x = "John"
x = 'John'

# Variable Names are CASE sensitive
a = 4
A = "Sally"
print(a, A) # Expected Output = 4 Sally

# Legal Variable Names:
myvar = "Legal"
my_var = "Legal"
_my_var = "Legal"
myVar = "Legal"
MYVAR = "Legal"
myvar2 = "Legal"

"""
# Illegal Variable Names:
2myvar = "Illegal" # Variable Name Cannot Start with a Number
my-var = "Illegal" # Variable Name Cannot Contain a - (Hyphen)
my var = "Illegal" # Variable Name Cannot Contain a Space
"""

#Variable Naming Standards (Optionally Obligated)
# Camel Case:
myVariableName = "camelCase"
# Pascal Case:
MyVariableName = "PascalCase"
# Snake Case
my_variable_name = "snake_case"

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x) # Expected Output = Orange
print(y) # Expected Output = Banana
print(z) # Expected Output = Cherry

# One Value to Multiple Variables
x = y = z = "Orange"
print(x) # Expected Output = Orange
print(y) # Expected Output = Orange
print(z) # Expected Output = Orange

# Unpack a Collection
fruits = ["Apple","Banana","Cherry"]
x, y, z = fruits
print(x) # Expected Output = Apple
print(y) # Expected Output = Banana
print(z) # Expected Output = Cherry

# Output Variables
x = "Out"
y = "put"
print(x, y) # Expected Output = Out put
print(x + y) # Expected Output = Output


x = 5
y = "Five"
"""
print(x + y) # Expected Output = ERROR (Cannot Add Int and String Together)
"""
print(x, y) # Expected Output = 5 Five (, (Comma) isn't Math Operator)

# Global Variables
x = "GlobalVariable"

def myFunc():
    print(x)

myFunc() # Expected Output = Global Variable

# Global Variable Overwritten
x = "GlobalVariable2"

def myFunc2():
    x = "Overwritten"
    print(x)

myFunc2() # Expected Output = Overwritten
print(x) # Expected Output = GlobalVariable2

# Global Keyword
x = "GlobalVariable3"
def myFunc3():
    global x
    x = "GlobalOverwrittenVariable"
myFunc3()
print(x)