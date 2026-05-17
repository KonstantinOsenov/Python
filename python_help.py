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

# One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

# Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y # new tuple
print(thistuple)

# Using Asterisk*
# Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
# If the asterisk is added to another variable name than the last, 
# Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# Join two tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply the fruits tuple by 2:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

# Tuple Methods
# count() | Returns the number of times a specified value occurs in a tuple
# index() | Searches the tuple for a specified value and returns the position of where it was found

#################################
#### Python Sets
#################################
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

# Duplicates Not Allowed
# True and 1 is considered the same value
# False and 0 is considered the same value
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# If the item to remove does not exist, remove() will raise an error.

# Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# If the item to remove does not exist, discard() will NOT raise an error.

# Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
# Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

# There are several ways to join two or more sets in Python.

## The union() and update() methods joins all items from both sets.

### Join set1 and set2 into a new set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

### You can use the | operator instead of the union() method, and you will get the same result.
### Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

### Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.
# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

## The intersection() method keeps ONLY the duplicates.

### The intersection() method will return a new set, that only contains the items that are present in both sets.
### Join set1 and set2, but keep only the duplicates:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
### You can use the & operator instead of the intersection() method, and you will get the same result.

### The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
### Keep the items that exist in both set1, and set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

## The difference() method keeps the items from the first set that are not in the other set(s).

### The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
### Keep all items from set1 that are not in set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
### You can use the - operator instead of the difference() method, and you will get the same result.

### The difference_update() method will keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
### Use the difference_update() method to keep only the items from the first set that are not present in the other set:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

## The symmetric_difference() method keeps all items EXCEPT the duplicates.
### The symmetric_difference() method will keep only the elements that are NOT present in both sets.
### Keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
### You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

### The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
### Use the symmetric_difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

# frozenset is an immutable version of a set.
# Create a frozenset and check its type:
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

# Frozenset Methods
# copy()	 			Returns	a shallow copy	
# difference()	-		Returns a new frozenset with the difference	
# intersection() &		Returns a new frozenset with the intersection	
# isdisjoint()	 		Returns True if there is NO intersection between two frozensets	
# issubset() <= / <		Returns True if this frozenset is a (proper) subset of another	
# issuperset() >= / >	Returns True if this frozenset is a (proper) superset of another	
# symmetric_difference() ^ Returns a new frozenset with the symmetric differences	
# union()	|			Returns a new frozenset containing the union

# Set Methods

# add()	 			Adds an element to the set
# clear()	 			Removes all the elements from the set
# copy()	 			Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 		Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update() &=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns True if NO items of this set is present in another set
# issubset()	<=		Returns True if all items of this set is present in another set
# 				<		Returns True if all items of this set is present in another, larger set
# issuperset()	>=	Returns True if all items of another set is present in this set
# 				>	Returns True if all items of another, smaller set is present in this set
# pop()	 			Removes an element from the set
# remove()	 		Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()		|		Return a set containing the union of sets
# update()	|=		Update the set with the union of this set and others

# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries cannot have two items with the same key:

# Create and print a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

# Get the value of the "model" key:
x = thisdict.get("model")

# Get a list of the keys:
x = thisdict.keys()

# Get a list of the values:
x = thisdict.values()

# Get a list of the key:value pairs
x = thisdict.items()

# Change the "year" to 2018:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# Add a color item to the dictionary by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

# The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# The del keyword can also delete the dictionary completely:
del thisdict

# The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)

# You cannot copy a dictionary simply by typing dict2 = dict1, 
# because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Make a copy of a dictionary with the dict() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Access Items in Nested Dictionaries
# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
# Print the name of child 2:
print(myfamily["child2"]["name"])

# Dictionary Methods

# clear()	|	Removes all the elements from the dictionary
# copy()	|	Returns a copy of the dictionary
# fromkeys()	|	Returns a dictionary with the specified keys and value
# get()	|	Returns the value of the specified key
# items()	|	Returns a list containing a tuple for each key value pair
# keys()	|	Returns a list containing the dictionary's keys
# pop()	|	Removes the element with the specified key
# popitem()	|	Removes the last inserted key-value pair
# setdefault()	|	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	|	Updates the dictionary with the specified key-value pairs
# values()	|	Returns a list of all the values in the dictionary



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




