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

# Specify a Variable Type

# Int
x = int(2) # Expected Output = 1
y = int(2.8) # Expected Output = 2
z = int("3") # Expected Output = 3
# Float
x = float(1) # Expected Output = 1.0
y = float(2.8) # Expected Output = 2.8
z = float("3") # Expected Output = 3.0
w = float("4.2") # Expected Output = 4.2
# Strings
x = str("s1") # Expected Output = "s1"
y = str(2) # Expected Output = "2"
z = str(3.0) # Expected Output = "3.0"

"""Quotes Inside Quotes are allowed,
as long as they don't match the quotes,
surrounding the string
"""
print("It's Allowed")
print("This is 'Allowed")
print('This is "Allowed"')

# Multiline Strings
a = """This is a Multiline String.
it is meant to help when having to 
type a long sentence and print it"""
print(a)

a = '''This is a Multiline String.
it is meant to help when having to 
type a long sentence and print it'''
print(a)

"""
Strings in Python are Arrays of Bytes
representing Unicode Characters.

Python does not have a character datatype,
a single character is simply a string with 
a length of 1
"""

a = "Hello, World"
print(a[1]) # Expected Output = e (H is index position '0')

# Looping through a String
for x in "banana":
    print(x)

# String Length
a = "Hello, World"
print(len(a)) # Expected Output = 12 (',' and ' ' are counted as characters in string)

# Check String (Is 'is' present in txt)
txt = "This is a sentence"
print("is" in txt)
    # If Statement
txt = "This is a sentence"
if "is" in txt:
    print("OOGA BOOGA")

# Check if Not (Is 'is' not in txt)
txt = "This is a sentence"
print("isn't" not in txt)
# If Statement
if "is" not in txt:
    print("OOGA BOOGA")
else:
    print("BOOGA OOGA")

"""
Slicing. To return a range of characters by using the slice syntax,
Specify the start index and the end index, seperated by a colon ',',
to return a part of the string
"""

#Slicing
b = "Yo What's Up"
print(b[1:6]) # Expected Output = 0 Wha - 1 2 345

# Slice from the Start
b = "Yo What's Up"
print(b[:6]) # Expected Output = Yo Wha - 01 2 345

# Slice to the End
b = "Yo What's Up"
print(b[2:]) # Expected Output =  What's Up - 2 345678 9 AB

# Negative Indexing. To start the slice from the end of the string
b = "Yo What's Up"
print(b[-5:-2]) # Expected Output = 's - 78

"""
Explanation:
-1 Refers to the last character.
-2 Refers to the second last.
"""

# Uppercase
a = "Hello World"
print(a.upper()) # Expected Output = HELLO WORLD

# Lowercase
a = "HELLO WORLD"
print(a.lower()) # Expected Output = hello world

# Remove White Space / Empty Space / Negative Space
a = "  Hello WOR L d"
print(a.strip()) # Expected Output = Hello WOR L d

# Replace String
a = "Car Sales Person"
print(a.replace("C", "R")) # Expected Output = Rar Sales Person

# Split String
"""
Split String. ',' Comma is the seperator and the sentence is split
"""
a = "Hello, World!"
print(a.split(",")) # Expected Output ['Hello' ',' 'World!']

# String Concatenation
a = "String"
b = "Concatenation"
c = a + b
print(c) # Expected Output = StringConcatenation

a = "Hello"
b = "World"
c = a + " " + b # Expected Output = String Concatenation

"""
# String Format
age = 36
txt = "Age: " + age
print(txt) # Expected Output = Error Cannot Concatenate Strings and Ints at same time
"""

# F-Strings
# Specify F-String put F infront of the String Literal and add curly brackets {} as placeholders
age = 36
txt = f"Age: {age}"
print(txt) # Expected Output = Age: 36

#Placeholders and Modifiers
price = 59
txt = f"Price: {price} £'s"
print(txt)

# Display Price with 2 Decimals
price = 59
txt = f"Price {price:.2f} £'s"
print(txt) # Expected Output = Price 59.00 £'s

# Math Operation in Placeholder
txt = f"Price: {20 * 59} £'s"
print(txt) # Expected Output = Price 1180 £'s

# Escape Character
#txt = "I am "Illegal"" # Expected Output = Error
txt = "I am \"Legal\""
print(txt)# Expected Output = I am "Legal"

# Escape Characters:
# \'
txt = 'I am \'Single Quote\''
print(txt) # Expected Output = I am 'Single Quote'
# \\
txt = "I am Backslash\\Slashback"
print(txt)  # Expected Output = I am Backslash\Slashback
#\n
txt = "I am \n New Line"
print(txt) # Expected Output = I am (Next Line) New Line
#\r
txt = "I am \r Carriage Return"
print(txt) # Expected Output = I am (Next Line) Carriage Return
#\t
txt = "I am \t Tab"
print(txt) # Expected Output = I am    tab
#\b
txt = "I am \b Backspace" # Expected Output = I amBackspace
print(txt) # Expected Output = I amBackspace
#\f
txt = "I am \f Form Feed"
print(txt) # Expected Output =
#\000 (Numbers not Letters)
txt = "I am \000 Octal Value"
print(txt) # Expected Output = I am 000 Octal Value
#\xhh
txt = "I am \x00 Hex Value"
print(txt) # Expected Output = I am 00 Hex Value

