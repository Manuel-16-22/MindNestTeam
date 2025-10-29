#STRINGS practice

a = " manuel,AI enginer "
b = "that boy di bad "
e = 21
f = "04"
print(a)
#string - slicing
#this is to print certain parts of a string, using negative (-) starts
# from the end of the string
print(a[2:8])
print(a[-9:-2])
#string - modify
#this is to convert from one string type to another
print(a.upper())
print(a.strip())
print(a.lower())
print(a.count("e"))
print(a.replace("manuel", "Dice"))
print(a.split(","))
#string - concatenate
#used to join 2 or more strings together
c = a + b
print(c)
#string -  f-strings
# used to combine strings and numbers
print(f"{a} {b} at {e}")
#string - escape characters
print(f" man i've been \"bad\" since '{f} ")
print(15 % 4 )


## OPERATORS - Operators are used to perform operations on variables and values.
#assignment operators
if (count:= len(a)) > 3:
    print(F" there are {count} letters in string a")
x = 10
y = 20

##logical operators
print(f"{x} {y} at {x*y}")
print(x > y or x < y)
print(x > y and x < y)
##Identity operators - are used to compare the objects, not if they are equal,
#    but if they are actually the same object, with the same memory location.
# is and ==
print(x == y)
print(x is y)

#membership operators- "in" and "not in", can be used for both strings and lists
# used to check whether there is a value in a sequence.

## Bitwise Operators
# used for boolean comparison; &, ^, |, ~, >>, <<
print(6 & 3)  #converts to binary and then performs the '&'
print(6 | 3)
print(6 ^ 3)

##Operator precedence
# Operator precedence describes the order in which operations are performed.
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
print(5 + 4 - 7 + 3)


###DATA TYPES
##LISTS - this is one of the four collection data types in python
# it is ordered and changeable and allows duplicate members.
list1 = [ 'chibunna ', 'Agozie', 'santana' ]
if 'santana' in list1:
    print("santana dey there oh")
for x in list1:
    print(x)
list1.append("sikki ")
list1.sort()
print(list1)
list1.reverse()
print(list1)

##TUPLE - this is anoda type of collection in python
# it is ordered and unchangeable, written in round brackets.
tuple1 = ("Chifa", "Ronny", "Emzee", "Bigila")
print("this will help u check ppl wey dey the group ")
name = input("abeg enter name of pesin u wan check: \n" ).lower()
tuple_lower = tuple(x.lower() for x in tuple1)
if name in tuple_lower:
    print(f"yes ohh, {name} dey the group")
else:
    print("nope, him no dey the group")







