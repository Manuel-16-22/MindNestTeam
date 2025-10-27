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



