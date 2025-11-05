##functions - A function is a block of code which only runs when it is called.
#A function can return data as a result. An argument is the actual value that is sent to the function when it is called.
#A function helps to avoid code repetition.
#A parameter is the variable listed inside the parentheses in the function definition.

def family_name(name): #name is a parameter
    print(name + "Ali")
family_name("Gloria ")#Gloria is an argument
family_name("Jennifer ")
family_name("Christian ")

#functions accepts different data types, example: lists;
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])
my_person = {"name": "Dicey", "age": 21}
my_function(my_person)

## functions can also return values using the return statement
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)
# sometimes you may not know how many arguments that will
# be passed into your function.
#*args and **kwargs allow functions to accept an unknown number of arguments.

#Arbitrary arguments *args
def my_function(*kids):#kids - positional argument
    print("the second child dey " + kids[1])
my_function("jonze", "mumu", "gbezome")

#Arbitrary keyword arguments **kwargs
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")
## A variable is only available from inside the region it was created
## This is called Scope
def my_function():
    x = 10
    y = 20
    print(x)
    print(y)
my_function()
##Global variable-is a variable created in the main body
## it belongs to the global scope but can be accessed from any scope, local or global.
x = 300
def myfunc():
  x = 200
  print(x)
myfunc()
print(x)
print()
## python Decorators
def changecase(func):
    def changer():
        return func().upper()
    return changer
@changecase
def change1():
    return "Dicey"
@changecase
def change2():
    return "SiKKi"
print(change1())
print(change2())
print()
###########################################################
#Decorators can accept their own arguments by adding another wrapper level.
def changecase(n):
    def changer(change1):
        def changerif():
            if n == 1:
                a = change1().upper()
            else:
                a = change1().lower()
            return a
        return changerif
    return changer
@changecase(1)
def myfunction():
  return "Hello Linus"
print()
print(myfunction())
## a function's name can be returned with the __name__ attribute:
def myfunction():
  return "Have a great day!"
print(myfunction.__name__)

                            ##Lambda Function
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mytripler(11))
print()

##lambda functions with python built-in functions
#map() function - the map() function applies a function to every item in an iterable:
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
## filter() function
# the filter() function creates a list of items for which a function returns True:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
even_numbers = list(map(lambda y: y % 2 == 0, numbers))
print("the true values are even numbers;")
print(even_numbers)
print()
## sorted function
#the sorted() function can use a lambda as a key for custom sorting:
words = ["apple", "pie", "banana", "cherry"]
print(words)
print(" sorted according to length of words")
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
## Recursion- this is when a function calls itself
#Every recursive function must have two parts:
#A base case - A condition that stops the recursion
#A recursive case - The function calling itself with a modified argument
#Without a base case, the function would call itself forever, causing a stack overflow error.
                #fibonacci sequence
def fibonacci(n):
  if n <= 1: #base case
    return n
  else: #recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))


