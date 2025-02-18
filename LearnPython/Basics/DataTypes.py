"""
Text Type - str (String)

Numeric Types - int (Integer)
              - float ()
              - complex ()

Sequence Types - list ()
               - tuple ()
               - range ()

Mapping Types - dict ()

Set Types - set ()
          - frozenset ()

Boolean Type - bool ()

Binary Types - bytes
             - bytearray
             - memoryview

None Type - NoneType
"""

# Getting Data Type
x = 5
print(type(x)) # Expected Output = <class 'int'>

# Setting Data Type

# String
x = "String" # str
x = str("String") # str

# Int
x = 20 # int
x = int(20) # int

# Complex
x = 1j # complex
x = complex(1j) # complex

# List
x = ["Apple", "Banana", "Cherry"] # list
x = list(["Apple", "Banana", "Cherry"]) # list

# Tuple
x = ("apple", "banana", "cherry") # tuple
x = tuple(("apple", "banana", "cherry")) # tuple

# Range
x = range(6) # range

# Dict
x = {"name" : "John", "Age" : 36} # dict
x = dict({"name" : "John", "Age" : 36}) # dict

# Set
x = {"apple", "banana", "cherry"} # set
x = set(("apple", "banana", "cherry")) #set

# Frozenset
x = frozenset({"apple", "banana", "cherry"}) # frozenset
x = frozenset(("apple", "banana", "cherry")) # frozenset

# Boolean
x = True # bool
x = bool(5) # bool

# Bytes
x = bytes(5) # bytes

# Byte Array
x = bytearray(5) # bytearray

# Memory View
x = memoryview(bytes(5)) # memoryview

# None Type
x = None # NoneType

x = 1  # int
y = 2.8 # float
z = 1j # complex

# Int
"""
Int (Integer) is a whole number,
Positive or Negative,
Without Decimals,
with Unlimited Length.
"""
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Float
"""
Float (Floating Point Number),
is a number, positive or negative,
containing one or more decimals.
"""
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

"""
Float can also be scientific numbers,
with an 'e' to indicate the power of 10.
"""
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Complex
"""Complex numbers are written,
with 'j' as the imaginary part.
"""
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Type Conversion
"""
You can Convert from one type to another,
with the int(), float() and complex(),
methods.
"""

x = 1
y = 2.8
z = 1j

# Convert from int to float:
a = float(x)
print(a) # Expected Output = 1.0

# Convert from float to int:
b = int(y)
print(b) # Expected Output = 2

# Convert from int to complex:
c = complex(x)
print(c) # Expected Output = 1+0j

# Random Number
import random # Import the Built-in Module (Usually at the top)

print(random.randrange(1,10))
# Expected Output is any number between 1 and 10

