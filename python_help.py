#################################
## variables
#################################
x = "Cherry"
x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange"
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
# global keyword
global x
x = "fantastic"

#################################
## data types
#################################
type(x)
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

#################################
#### Numeric Types:	int, float, complex
#################################
import random
print(random.randrange(1, 10))

#################################
#### Text Type:	str
#################################
len("Hello, World!") # String Length
print("free" in "The best things in life are free!") # Check String

# multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit"""

# slicing
b = "Hello, World!"
print(b[2:5]) # Get the characters from position 2 to position 5 (not included)
print(b[:5])
print(b[2:])
print(b[-5:-2])

# methods
a = "qwerty"
a.capitalize() 		# Converts the first character to upper case
a.casefold() 		# Converts string into lower case
a.center() 			# Returns a centered string
a.count() 			# Returns the number of times a specified value occurs in a string
a.encode() 			# Returns an encoded version of the string
a.endswith() 		# Returns true if the string ends with the specified value
a.expandtabs() 		# Sets the tab size of the string
a.find() 			# Searches the string for a specified value and returns the position of where it was found
a.format() 			# Formats specified values in a string
a.format_map() 		# Formats specified values in a string
a.index() 			# Searches the string for a specified value and returns the position of where it was found
a.isalnum() 		# Returns True if all characters in the string are alphanumeric
a.isalpha() 		# Returns True if all characters in the string are in the alphabet
a.isascii() 		# Returns True if all characters in the string are ascii characters
a.isdecimal() 		# Returns True if all characters in the string are decimals
a.isdigit() 		# Returns True if all characters in the string are digits
a.isidentifier() 	# Returns True if the string is an identifier
a.islower() 		# Returns True if all characters in the string are lower case
a.isnumeric() 		# Returns True if all characters in the string are numeric
a.isprintable() 	# Returns True if all characters in the string are printable
a.isspace() 		# Returns True if all characters in the string are whitespaces
a.istitle() 		# Returns True if the string follows the rules of a title
a.isupper() 		# Returns True if all characters in the string are upper case
a.join() 			# Joins the elements of an iterable to the end of the string
a.ljust() 			# Returns a left justified version of the string
a.lower() 			# Converts a string into lower case
a.lstrip() 			# Returns a left trim version of the string
a.maketrans() 		# Returns a translation table to be used in translations
a.partition() 		# Returns a tuple where the string is parted into three parts
a.replace() 		# Returns a string where a specified value is replaced with a specified value
a.rfind() 			# Searches the string for a specified value and returns the last position of where it was found
a.rindex() 			# Searches the string for a specified value and returns the last position of where it was found
a.rjust() 			# Returns a right justified version of the string
a.rpartition() 		# Returns a tuple where the string is parted into three parts
a.rsplit() 			# Splits the string at the specified separator, and returns a list
a.rstrip() 			# Returns a right trim version of the string
a.split() 			# Splits the string at the specified separator, and returns a list
a.splitlines() 		# Splits the string at line breaks and returns a list
a.startswith() 		# Returns true if the string starts with the specified value
a.strip() 			# Returns a trimmed version of the string
a.swapcase() 		# Swaps cases, lower case becomes upper case and vice versa
a.title() 			# Converts the first character of each word to upper case
a.translate() 		# Returns a translated string
a.upper() 			# Converts a string into upper case
a.zfill() 			# Fills the string with a specified number of 0 values at the beginning

#################################
#### Boolean Type:	bool
#################################
# Almost any value is evaluated to True if it has some sort of content.
# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. 

#################################
#### Python Lists
#################################
# List is a collection which is ordered and changeable. Allows duplicate members.
# Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Remove "banana":
# If there are more than one item with the specified value, the remove() method removes the first occurrence:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# If you do not specify the index, the pop() method removes the last item.

# Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]

# Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
thislist.sort(reverse = True)
print(thislist)

# Customize Sort Function
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist.sort(key = str.lower)

# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
mylist = list(thislist) # list method
mylist = thislist[:] # slice operator

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# List Methods
# append()		Adds an element at the end of the list
# clear()		Removes all the elements from the list
# copy()		Returns a copy of the list
# count()		Returns the number of elements with the specified value
# extend()		Add the elements of a list (or any iterable), to the end of the current list
# index()		Returns the index of the first element with the specified value
# insert()		Adds an element at the specified position
# pop()			Removes the element at the specified position
# remove()		Removes the item with the specified value
# reverse()		Reverses the order of the list
# sort()		Sorts the list

#################################
#### Python Tuples
#################################
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.



# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.









#################################
## Operators
#################################
# +	Addition | x + y	
# -	Subtraction | x - y	
# *	Multiplication | x * y	
# /	Division | x / y	
# %	Modulus | x % y	
# **	Exponentiation | x ** y	
# //	Floor division | x // y	
# :=	print(x := 3) | x = 3; print(x)

#################################
## 
#################################




