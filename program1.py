#A program that grades a student
score = int(input("enter your score  "))
attendance = int(input("enter your attendance percentage  "))
if score < 0 or score > 100 or attendance < 0 or attendance > 100:
    print("Invalid input! Please enter values between 0 and 100.")

if score >= 80 and attendance >= 90:
    print("you passed")
elif score >= 50 and attendance >= 75 :
    print("you barely passed")
else :
    print("you failed")