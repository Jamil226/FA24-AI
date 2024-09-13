#------------------------------
# Simple Function Definition
#------------------------------

def hello_world():
  print("Hello from a function")
# Calling a Function
hello_world()

#------------------------------
# Function Arguments
#------------------------------

def my_function(fname):
  print(fname + " Khan")

my_function("Abdullah")
my_function("Ahmad")

#------------------------------
# Arbitrary Arguments, *args
#------------------------------

def my_function(fname, lname):
  print(fname + "\n" + lname)

my_function("Ahmad", "Ali")

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Ali", "Ahmad", "Abid", "Asif")

#------------------------------
# Keyword Arguments
#------------------------------


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
  print("The elder child is " + child2)
  print("The middle child is " + child1)

my_function(child1 = "Abid", child2 = "Ali", child3 = "Alisha")

#------------------------------
# Arbitrary Keyword Arguments, **kwargs
#------------------------------

def my_function(**kid):
  print("His last name is " + kid["last_name"])

my_function(first_name = "Ahmad", last_name = "Hassan")

#------------------------------
# Default Parameter Value
#------------------------------

def my_function(country = "Norway"):
  print("I am from " + country)

my_function()
my_function("Pakistan")

#------------------------------
# Passing a List as an Argument
#------------------------------

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#------------------------------
# Return Values
#------------------------------

def my_function(x):
  return 5 * x

print(my_function(3))


