### IF - ELSE
# this is used to evaluate conditions and give the
#result as true or false. The codeblock inside is executed
#if statement is true and skipped otherwise.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

                #Nested if - else
passscore = 60
passattendance = 90
submitted = True
score = int(input("please enter your score: "))
attendance = int(input("what's your attendance score?: "))

if score >= passscore:
  if attendance >= passattendance:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

### WHILE LOOP
# this is used to execute a set of statements
#as long as the condition is true
#i = 1
#while i < 6:
#  print(i)
 # i += 1
#With the 'break' statement we can stop the loop
# even if the while condition is true:
#i = 1
#while i < 6:
 #   print(i)
  #  if i == 3:
   #     break
    #i += 1
#With the continue statement we can stop the current iteration,
# and continue with the next:
#i = 0
#while i < 6:
#  i += 1
#  if i == 3:
#    continue
#  print(i)

                   #while and else
number = 0
while number < 10:
    number += 1
    print(number)
else:
    print("number is no longer less than 10")

                 #for loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
